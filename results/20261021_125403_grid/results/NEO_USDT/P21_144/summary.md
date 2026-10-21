# EMA Hourly Continuation — NEO/USDT P21_144

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8103 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0159 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.0809 |
| sortino_ratio | -0.2827 |
| max_drawdown | 0.3643 |
| cagr | -0.1230 |
| net_avg_win | 70.9333 |
| net_avg_loss | -90.7648 |
| avg_hold_time_bars | 38.5000 |
| exposure | 0.5810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
