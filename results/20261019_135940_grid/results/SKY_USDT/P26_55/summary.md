# EMA Hourly Continuation — SKY/USDT P26_55

**Symbol:** SKY/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.4192 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8300 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -7.8242 |
| sortino_ratio | -3.3550 |
| max_drawdown | 0.9673 |
| cagr | -0.8087 |
| net_avg_win | 21.0671 |
| net_avg_loss | -39.3257 |
| avg_hold_time_bars | 5.0703 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
