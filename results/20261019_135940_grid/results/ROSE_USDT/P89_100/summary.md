# EMA Hourly Continuation — ROSE/USDT P89_100

**Symbol:** ROSE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.3044 |
| net_win_rate | 0.4044 |
| gross_profit_factor | 0.6980 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -8.4057 |
| sortino_ratio | -2.9402 |
| max_drawdown | 0.9782 |
| cagr | -0.7812 |
| net_avg_win | 17.7597 |
| net_avg_loss | -39.6056 |
| avg_hold_time_bars | 2.1527 |
| exposure | 0.0583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
