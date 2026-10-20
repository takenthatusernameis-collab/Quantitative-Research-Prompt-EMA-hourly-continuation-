# EMA Hourly Continuation — KAVA/USDT P20_200

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.6308 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -3.2862 |
| sortino_ratio | -0.9613 |
| max_drawdown | 0.6927 |
| cagr | -0.3633 |
| net_avg_win | 58.5258 |
| net_avg_loss | -80.2178 |
| avg_hold_time_bars | 32.9578 |
| exposure | 0.6397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
