# EMA Hourly Continuation — WEMIX/USDT P89_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.1642 |
| net_win_rate | 0.2245 |
| gross_profit_factor | 0.4254 |
| gross_win_rate | 0.2691 |
| sharpe_ratio | -17.0574 |
| sortino_ratio | -8.0517 |
| max_drawdown | 1.0000 |
| cagr | -0.9870 |
| net_avg_win | 9.3140 |
| net_avg_loss | -16.4130 |
| avg_hold_time_bars | 2.2926 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
