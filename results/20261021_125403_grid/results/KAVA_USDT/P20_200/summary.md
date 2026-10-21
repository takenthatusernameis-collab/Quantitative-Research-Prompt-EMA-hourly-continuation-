# EMA Hourly Continuation — KAVA/USDT P20_200

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.7279 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -1.8671 |
| sortino_ratio | -0.4921 |
| max_drawdown | 0.4485 |
| cagr | -0.2032 |
| net_avg_win | 70.0581 |
| net_avg_loss | -90.7784 |
| avg_hold_time_bars | 40.7398 |
| exposure | 0.6333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
