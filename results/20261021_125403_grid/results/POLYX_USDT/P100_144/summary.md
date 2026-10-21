# EMA Hourly Continuation — POLYX/USDT P100_144

**Symbol:** POLYX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6314 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.4146 |
| sortino_ratio | -0.6181 |
| max_drawdown | 0.5133 |
| cagr | -0.2467 |
| net_avg_win | 55.8966 |
| net_avg_loss | -85.2539 |
| avg_hold_time_bars | 6.0440 |
| exposure | 0.0874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
