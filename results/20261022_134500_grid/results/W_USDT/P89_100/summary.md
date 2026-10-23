# EMA Hourly Continuation — W/USDT P89_100

**Symbol:** W/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.3389 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7832 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -7.2596 |
| sortino_ratio | -2.5077 |
| max_drawdown | 0.9617 |
| cagr | -0.7257 |
| net_avg_win | 18.8106 |
| net_avg_loss | -43.7957 |
| avg_hold_time_bars | 2.1751 |
| exposure | 0.0587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
