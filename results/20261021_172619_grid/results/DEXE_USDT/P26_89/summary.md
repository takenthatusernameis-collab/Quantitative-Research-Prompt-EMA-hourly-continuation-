# EMA Hourly Continuation — DEXE/USDT P26_89

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7764 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 0.9834 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.4398 |
| sortino_ratio | -0.4161 |
| max_drawdown | 0.4208 |
| cagr | -0.1750 |
| net_avg_win | 64.8896 |
| net_avg_loss | -84.3983 |
| avg_hold_time_bars | 24.7108 |
| exposure | 0.4583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
