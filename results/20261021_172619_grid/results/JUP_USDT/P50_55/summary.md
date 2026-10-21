# EMA Hourly Continuation — JUP/USDT P50_55

**Symbol:** JUP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 1.0921 |
| net_win_rate | 0.5979 |
| gross_profit_factor | 1.4690 |
| gross_win_rate | 0.5979 |
| sharpe_ratio | 0.3030 |
| sortino_ratio | 0.0441 |
| max_drawdown | 0.1009 |
| cagr | 0.0168 |
| net_avg_win | 87.4528 |
| net_avg_loss | -119.0920 |
| avg_hold_time_bars | 4.8247 |
| exposure | 0.0213 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
