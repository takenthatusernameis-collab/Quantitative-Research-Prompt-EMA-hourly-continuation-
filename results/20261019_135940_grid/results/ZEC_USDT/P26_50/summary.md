# EMA Hourly Continuation — ZEC/USDT P26_50

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.4453 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -7.2055 |
| sortino_ratio | -3.0573 |
| max_drawdown | 0.9782 |
| cagr | -0.7819 |
| net_avg_win | 19.2972 |
| net_avg_loss | -34.8531 |
| avg_hold_time_bars | 3.4337 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
