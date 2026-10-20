# EMA Hourly Continuation — BOME/USDT P26_89

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.5953 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -3.8327 |
| sortino_ratio | -1.4097 |
| max_drawdown | 0.8340 |
| cagr | -0.4942 |
| net_avg_win | 36.6404 |
| net_avg_loss | -55.9374 |
| avg_hold_time_bars | 9.7366 |
| exposure | 0.3058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
