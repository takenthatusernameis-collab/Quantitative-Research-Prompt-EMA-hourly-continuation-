# EMA Hourly Continuation — PEPE/USDT P21_34

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.4369 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8965 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -9.9473 |
| sortino_ratio | -4.8045 |
| max_drawdown | 0.9978 |
| cagr | -0.9112 |
| net_avg_win | 15.1187 |
| net_avg_loss | -27.2165 |
| avg_hold_time_bars | 2.3689 |
| exposure | 0.1252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
