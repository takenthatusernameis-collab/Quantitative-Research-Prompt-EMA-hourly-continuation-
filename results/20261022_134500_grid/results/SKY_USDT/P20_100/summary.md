# EMA Hourly Continuation — SKY/USDT P20_100

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6846 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0610 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -3.3195 |
| sortino_ratio | -1.1511 |
| max_drawdown | 0.7706 |
| cagr | -0.4305 |
| net_avg_win | 58.6930 |
| net_avg_loss | -86.0737 |
| avg_hold_time_bars | 17.0535 |
| exposure | 0.4802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
