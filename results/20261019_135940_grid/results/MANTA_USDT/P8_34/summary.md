# EMA Hourly Continuation — MANTA/USDT P8_34

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1290 |
| net_profit_factor | 0.6203 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 1.0533 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -7.1601 |
| sortino_ratio | -3.6093 |
| max_drawdown | 0.9879 |
| cagr | -0.8279 |
| net_avg_win | 27.0769 |
| net_avg_loss | -37.4889 |
| avg_hold_time_bars | 6.9078 |
| exposure | 0.4050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
