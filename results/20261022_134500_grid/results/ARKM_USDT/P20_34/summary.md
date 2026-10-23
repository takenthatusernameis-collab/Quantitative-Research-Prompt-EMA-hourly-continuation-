# EMA Hourly Continuation — ARKM/USDT P20_34

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1172 |
| net_profit_factor | 0.5204 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.9604 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -8.8807 |
| sortino_ratio | -4.3061 |
| max_drawdown | 0.9952 |
| cagr | -0.8795 |
| net_avg_win | 20.8879 |
| net_avg_loss | -31.6792 |
| avg_hold_time_bars | 2.7534 |
| exposure | 0.1467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
