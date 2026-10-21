# EMA Hourly Continuation — NEO/USDT P89_144

**Symbol:** NEO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7019 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 0.9868 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -1.7431 |
| sortino_ratio | -0.4124 |
| max_drawdown | 0.3879 |
| cagr | -0.1717 |
| net_avg_win | 65.2370 |
| net_avg_loss | -93.6347 |
| avg_hold_time_bars | 7.3690 |
| exposure | 0.0908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
