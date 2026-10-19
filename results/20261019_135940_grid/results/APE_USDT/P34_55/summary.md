# EMA Hourly Continuation — APE/USDT P34_55

**Symbol:** APE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.4636 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9691 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -7.4888 |
| sortino_ratio | -3.2305 |
| max_drawdown | 0.9811 |
| cagr | -0.7932 |
| net_avg_win | 19.8534 |
| net_avg_loss | -36.7937 |
| avg_hold_time_bars | 2.8431 |
| exposure | 0.1194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
