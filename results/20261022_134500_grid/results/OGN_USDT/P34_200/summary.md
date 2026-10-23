# EMA Hourly Continuation — OGN/USDT P34_200

**Symbol:** OGN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6301 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.8768 |
| sortino_ratio | -0.7849 |
| max_drawdown | 0.6322 |
| cagr | -0.3098 |
| net_avg_win | 59.1517 |
| net_avg_loss | -82.1378 |
| avg_hold_time_bars | 31.7813 |
| exposure | 0.5393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
