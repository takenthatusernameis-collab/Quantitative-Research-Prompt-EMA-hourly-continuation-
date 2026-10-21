# EMA Hourly Continuation — BONK/USDT P34_200

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.9464 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0833 |
| gross_win_rate | 0.5249 |
| sharpe_ratio | -0.2223 |
| sortino_ratio | -0.0517 |
| max_drawdown | 0.1561 |
| cagr | -0.0275 |
| net_avg_win | 87.7986 |
| net_avg_loss | -100.9313 |
| avg_hold_time_bars | 41.1877 |
| exposure | 0.4886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
