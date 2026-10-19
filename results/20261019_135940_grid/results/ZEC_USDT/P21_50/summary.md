# EMA Hourly Continuation — ZEC/USDT P21_50

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.4541 |
| net_win_rate | 0.4456 |
| gross_profit_factor | 0.9488 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -7.0900 |
| sortino_ratio | -3.0314 |
| max_drawdown | 0.9777 |
| cagr | -0.7791 |
| net_avg_win | 19.6429 |
| net_avg_loss | -34.7701 |
| avg_hold_time_bars | 4.3961 |
| exposure | 0.1856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
