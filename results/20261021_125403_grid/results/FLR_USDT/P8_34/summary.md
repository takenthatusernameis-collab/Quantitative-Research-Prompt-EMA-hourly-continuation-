# EMA Hourly Continuation — FLR/USDT P8_34

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.6609 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -3.6213 |
| sortino_ratio | -1.4007 |
| max_drawdown | 0.8071 |
| cagr | -0.4731 |
| net_avg_win | 44.6691 |
| net_avg_loss | -61.7509 |
| avg_hold_time_bars | 8.4200 |
| exposure | 0.2798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
