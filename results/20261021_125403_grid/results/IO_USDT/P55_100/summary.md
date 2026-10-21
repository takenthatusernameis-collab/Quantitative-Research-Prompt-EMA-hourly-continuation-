# EMA Hourly Continuation — IO/USDT P55_100

**Symbol:** IO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.6676 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8321 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -2.1559 |
| sortino_ratio | -0.5536 |
| max_drawdown | 0.4660 |
| cagr | -0.2244 |
| net_avg_win | 64.1901 |
| net_avg_loss | -82.1667 |
| avg_hold_time_bars | 7.3954 |
| exposure | 0.1096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
