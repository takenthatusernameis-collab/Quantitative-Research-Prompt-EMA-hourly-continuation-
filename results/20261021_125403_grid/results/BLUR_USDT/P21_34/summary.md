# EMA Hourly Continuation — BLUR/USDT P21_34

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.4998 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.7071 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -3.8288 |
| sortino_ratio | -1.0408 |
| max_drawdown | 0.7165 |
| cagr | -0.3807 |
| net_avg_win | 44.9207 |
| net_avg_loss | -66.7712 |
| avg_hold_time_bars | 4.7923 |
| exposure | 0.0794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
