# EMA Hourly Continuation — DEXE/USDT P34_144

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.9170 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1147 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -0.3925 |
| sortino_ratio | -0.0974 |
| max_drawdown | 0.2480 |
| cagr | -0.0474 |
| net_avg_win | 80.3079 |
| net_avg_loss | -99.5468 |
| avg_hold_time_bars | 37.5051 |
| exposure | 0.5063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
