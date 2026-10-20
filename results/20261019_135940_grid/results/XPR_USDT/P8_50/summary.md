# EMA Hourly Continuation — XPR/USDT P8_50

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1155 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.8734 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -9.0304 |
| sortino_ratio | -4.2886 |
| max_drawdown | 0.9962 |
| cagr | -0.8881 |
| net_avg_win | 19.0366 |
| net_avg_loss | -29.5881 |
| avg_hold_time_bars | 7.9498 |
| exposure | 0.4174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
