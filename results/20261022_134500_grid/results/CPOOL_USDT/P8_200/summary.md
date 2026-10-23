# EMA Hourly Continuation — CPOOL/USDT P8_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.6645 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8387 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -2.9569 |
| sortino_ratio | -0.9625 |
| max_drawdown | 0.6961 |
| cagr | -0.3659 |
| net_avg_win | 54.2102 |
| net_avg_loss | -70.2863 |
| avg_hold_time_bars | 29.9721 |
| exposure | 0.7330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
