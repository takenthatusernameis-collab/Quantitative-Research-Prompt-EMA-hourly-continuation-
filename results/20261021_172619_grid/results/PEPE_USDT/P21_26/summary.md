# EMA Hourly Continuation — PEPE/USDT P21_26

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 135 |
| net_profit_factor | 0.7729 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0204 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -0.9617 |
| sortino_ratio | -0.1605 |
| max_drawdown | 0.2281 |
| cagr | -0.0710 |
| net_avg_win | 84.5519 |
| net_avg_loss | -111.0304 |
| avg_hold_time_bars | 4.4741 |
| exposure | 0.0275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
