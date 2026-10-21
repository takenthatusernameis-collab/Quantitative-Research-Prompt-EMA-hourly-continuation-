# EMA Hourly Continuation — ARKM/USDT P26_200

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.7891 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -1.2700 |
| sortino_ratio | -0.3209 |
| max_drawdown | 0.3828 |
| cagr | -0.1386 |
| net_avg_win | 77.4601 |
| net_avg_loss | -90.3771 |
| avg_hold_time_bars | 38.7079 |
| exposure | 0.5542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
