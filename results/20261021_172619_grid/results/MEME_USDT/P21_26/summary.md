# EMA Hourly Continuation — MEME/USDT P21_26

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.6279 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -2.3619 |
| sortino_ratio | -0.5126 |
| max_drawdown | 0.4958 |
| cagr | -0.2092 |
| net_avg_win | 70.2342 |
| net_avg_loss | -97.3080 |
| avg_hold_time_bars | 4.4435 |
| exposure | 0.0465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
