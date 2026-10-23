# EMA Hourly Continuation — MOODENG/USDT P12_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8987 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.1055 |
| gross_win_rate | 0.5277 |
| sharpe_ratio | -0.6375 |
| sortino_ratio | -0.1757 |
| max_drawdown | 0.2489 |
| cagr | -0.0825 |
| net_avg_win | 89.6870 |
| net_avg_loss | -110.0487 |
| avg_hold_time_bars | 43.1238 |
| exposure | 0.7325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
