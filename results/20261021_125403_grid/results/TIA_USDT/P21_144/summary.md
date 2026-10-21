# EMA Hourly Continuation — TIA/USDT P21_144

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.9139 |
| net_win_rate | 0.5127 |
| gross_profit_factor | 1.0441 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -0.4652 |
| sortino_ratio | -0.1184 |
| max_drawdown | 0.1981 |
| cagr | -0.0567 |
| net_avg_win | 89.8584 |
| net_avg_loss | -103.4694 |
| avg_hold_time_bars | 39.4108 |
| exposure | 0.5625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
