# EMA Hourly Continuation — ALEX/USDT P34_100

**Symbol:** ALEX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.5024 |
| net_win_rate | 0.3973 |
| gross_profit_factor | 0.7930 |
| gross_win_rate | 0.4088 |
| sharpe_ratio | -5.6541 |
| sortino_ratio | -1.8054 |
| max_drawdown | 0.8977 |
| cagr | -0.5860 |
| net_avg_win | 43.4542 |
| net_avg_loss | -57.0170 |
| avg_hold_time_bars | 13.7390 |
| exposure | 0.3254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
