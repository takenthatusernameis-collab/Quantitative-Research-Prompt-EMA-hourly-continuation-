# EMA Hourly Continuation — OGN/USDT P89_144

**Symbol:** OGN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.5184 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.7440 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -3.6337 |
| sortino_ratio | -0.9531 |
| max_drawdown | 0.6878 |
| cagr | -0.3581 |
| net_avg_win | 48.6342 |
| net_avg_loss | -72.4247 |
| avg_hold_time_bars | 7.5029 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
