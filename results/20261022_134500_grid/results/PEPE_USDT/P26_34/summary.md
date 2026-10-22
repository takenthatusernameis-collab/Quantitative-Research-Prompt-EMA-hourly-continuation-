# EMA Hourly Continuation — PEPE/USDT P26_34

**Symbol:** PEPE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1066 |
| net_profit_factor | 0.3641 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.8214 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -11.2885 |
| sortino_ratio | -5.2671 |
| max_drawdown | 0.9990 |
| cagr | -0.9354 |
| net_avg_win | 12.8554 |
| net_avg_loss | -25.2985 |
| avg_hold_time_bars | 1.8565 |
| exposure | 0.0900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
