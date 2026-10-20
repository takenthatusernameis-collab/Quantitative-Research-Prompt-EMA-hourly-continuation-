# EMA Hourly Continuation — TAIKO/USDT P34_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6060 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8927 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.7234 |
| sortino_ratio | -1.1360 |
| max_drawdown | 0.7371 |
| cagr | -0.4231 |
| net_avg_win | 53.9310 |
| net_avg_loss | -76.4938 |
| avg_hold_time_bars | 18.1511 |
| exposure | 0.3924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
