# EMA Hourly Continuation — CYBER/USDT P55_89

**Symbol:** CYBER/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8121 |
| net_win_rate | 0.5427 |
| gross_profit_factor | 1.1632 |
| gross_win_rate | 0.5427 |
| sharpe_ratio | -1.2238 |
| sortino_ratio | -0.3533 |
| max_drawdown | 0.3889 |
| cagr | -0.1501 |
| net_avg_win | 67.1231 |
| net_avg_loss | -98.0904 |
| avg_hold_time_bars | 6.1131 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
