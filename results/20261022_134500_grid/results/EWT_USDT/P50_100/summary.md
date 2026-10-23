# EMA Hourly Continuation — EWT/USDT P50_100

**Symbol:** EWT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.4315 |
| net_win_rate | 0.4177 |
| gross_profit_factor | 0.7165 |
| gross_win_rate | 0.4244 |
| sharpe_ratio | -6.1433 |
| sortino_ratio | -2.0952 |
| max_drawdown | 0.9293 |
| cagr | -0.6455 |
| net_avg_win | 28.5729 |
| net_avg_loss | -47.4914 |
| avg_hold_time_bars | 5.9032 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
