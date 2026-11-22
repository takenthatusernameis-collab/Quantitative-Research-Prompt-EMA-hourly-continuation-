# EMA Hourly Continuation — AZERO/USDT P8_21

**Symbol:** AZERO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1463 |
| net_profit_factor | 0.3991 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -10.9527 |
| sortino_ratio | -5.8790 |
| max_drawdown | 0.9994 |
| cagr | -0.9480 |
| net_avg_win | 11.0276 |
| net_avg_loss | -19.3181 |
| avg_hold_time_bars | 3.6398 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
