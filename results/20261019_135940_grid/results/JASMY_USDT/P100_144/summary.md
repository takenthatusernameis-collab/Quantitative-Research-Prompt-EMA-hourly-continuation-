# EMA Hourly Continuation — JASMY/USDT P100_144

**Symbol:** JASMY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5811 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -3.6905 |
| sortino_ratio | -1.1504 |
| max_drawdown | 0.7551 |
| cagr | -0.4289 |
| net_avg_win | 42.7632 |
| net_avg_loss | -74.4969 |
| avg_hold_time_bars | 4.4230 |
| exposure | 0.0979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
