# EMA Hourly Continuation — PROM/USDT P20_26

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1205 |
| net_profit_factor | 0.2935 |
| net_win_rate | 0.3627 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -13.9750 |
| sortino_ratio | -6.9957 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 9.5065 |
| net_avg_loss | -18.4290 |
| avg_hold_time_bars | 2.4174 |
| exposure | 0.1324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
