# EMA Hourly Continuation — DOT/USDT P89_200

**Symbol:** DOT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.9029 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -3.7854 |
| sortino_ratio | -1.0226 |
| max_drawdown | 0.7184 |
| cagr | -0.3944 |
| net_avg_win | 50.6384 |
| net_avg_loss | -78.4633 |
| avg_hold_time_bars | 10.0512 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
