# EMA Hourly Continuation — ALEX/USDT P21_100

**Symbol:** ALEX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.5876 |
| net_win_rate | 0.4335 |
| gross_profit_factor | 0.8597 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -4.6818 |
| sortino_ratio | -1.4923 |
| max_drawdown | 0.8555 |
| cagr | -0.5211 |
| net_avg_win | 52.6503 |
| net_avg_loss | -68.5580 |
| avg_hold_time_bars | 20.1521 |
| exposure | 0.4818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
