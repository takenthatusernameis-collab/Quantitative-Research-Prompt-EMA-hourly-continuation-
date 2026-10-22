# EMA Hourly Continuation — BONK/USDT P50_100

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.5720 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8821 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -4.6894 |
| sortino_ratio | -1.6252 |
| max_drawdown | 0.8701 |
| cagr | -0.5483 |
| net_avg_win | 41.5325 |
| net_avg_loss | -59.9013 |
| avg_hold_time_bars | 6.3463 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
