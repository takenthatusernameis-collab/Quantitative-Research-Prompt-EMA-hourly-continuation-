# EMA Hourly Continuation — POPCAT/USDT P26_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.8283 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -4.8407 |
| sortino_ratio | -1.8522 |
| max_drawdown | 0.8521 |
| cagr | -0.5870 |
| net_avg_win | 46.5774 |
| net_avg_loss | -60.6989 |
| avg_hold_time_bars | 9.3281 |
| exposure | 0.3139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
