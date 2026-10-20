# EMA Hourly Continuation — DEXE/USDT P26_50

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.3209 |
| net_win_rate | 0.3985 |
| gross_profit_factor | 0.6430 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -9.1503 |
| sortino_ratio | -3.9174 |
| max_drawdown | 0.9929 |
| cagr | -0.8599 |
| net_avg_win | 12.8548 |
| net_avg_loss | -26.5337 |
| avg_hold_time_bars | 6.6550 |
| exposure | 0.2771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
