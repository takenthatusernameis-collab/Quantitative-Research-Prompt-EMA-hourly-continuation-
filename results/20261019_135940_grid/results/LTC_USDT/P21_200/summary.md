# EMA Hourly Continuation — LTC/USDT P21_200

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.4194 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7811 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -4.5439 |
| sortino_ratio | -1.2609 |
| max_drawdown | 0.7986 |
| cagr | -0.4593 |
| net_avg_win | 34.0226 |
| net_avg_loss | -59.9423 |
| avg_hold_time_bars | 34.6921 |
| exposure | 0.6197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
