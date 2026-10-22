# EMA Hourly Continuation — ALEX/USDT P8_100

**Symbol:** ALEX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8667 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -3.9581 |
| sortino_ratio | -1.2167 |
| max_drawdown | 0.7883 |
| cagr | -0.4452 |
| net_avg_win | 52.0437 |
| net_avg_loss | -69.1472 |
| avg_hold_time_bars | 32.4639 |
| exposure | 0.7157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
