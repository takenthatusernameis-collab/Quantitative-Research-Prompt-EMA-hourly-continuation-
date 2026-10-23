# EMA Hourly Continuation — MINA/USDT P34_100

**Symbol:** MINA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.6423 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0309 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -3.3256 |
| sortino_ratio | -1.1445 |
| max_drawdown | 0.7962 |
| cagr | -0.4252 |
| net_avg_win | 45.5751 |
| net_avg_loss | -69.7720 |
| avg_hold_time_bars | 12.3953 |
| exposure | 0.3364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
