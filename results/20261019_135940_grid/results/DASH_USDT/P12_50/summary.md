# EMA Hourly Continuation — DASH/USDT P12_50

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.4173 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.9459 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -7.7817 |
| sortino_ratio | -3.5970 |
| max_drawdown | 0.9890 |
| cagr | -0.8338 |
| net_avg_win | 14.4271 |
| net_avg_loss | -28.0088 |
| avg_hold_time_bars | 6.8505 |
| exposure | 0.3416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
