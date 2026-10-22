# EMA Hourly Continuation — RENDER/USDT P8_34

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1253 |
| net_profit_factor | 0.5713 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9256 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -7.5309 |
| sortino_ratio | -4.0271 |
| max_drawdown | 0.9874 |
| cagr | -0.8609 |
| net_avg_win | 22.4259 |
| net_avg_loss | -34.4847 |
| avg_hold_time_bars | 4.9250 |
| exposure | 0.3257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
