# EMA Hourly Continuation — DEXE/USDT P26_34

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.7645 |
| net_win_rate | 0.5339 |
| gross_profit_factor | 1.1295 |
| gross_win_rate | 0.5339 |
| sharpe_ratio | -1.1568 |
| sortino_ratio | -0.2484 |
| max_drawdown | 0.2693 |
| cagr | -0.1077 |
| net_avg_win | 68.4424 |
| net_avg_loss | -102.5687 |
| avg_hold_time_bars | 13.7919 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
