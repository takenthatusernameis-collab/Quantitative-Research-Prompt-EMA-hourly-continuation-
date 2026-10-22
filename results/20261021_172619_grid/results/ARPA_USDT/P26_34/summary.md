# EMA Hourly Continuation — ARPA/USDT P26_34

**Symbol:** ARPA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5390 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -3.9677 |
| sortino_ratio | -1.0555 |
| max_drawdown | 0.7180 |
| cagr | -0.3853 |
| net_avg_win | 54.0211 |
| net_avg_loss | -79.8721 |
| avg_hold_time_bars | 5.0232 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
