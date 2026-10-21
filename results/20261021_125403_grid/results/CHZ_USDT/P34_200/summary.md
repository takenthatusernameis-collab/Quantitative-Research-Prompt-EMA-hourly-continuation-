# EMA Hourly Continuation — CHZ/USDT P34_200

**Symbol:** CHZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.9510 |
| net_win_rate | 0.5377 |
| gross_profit_factor | 1.1439 |
| gross_win_rate | 0.5377 |
| sharpe_ratio | -0.2078 |
| sortino_ratio | -0.0512 |
| max_drawdown | 0.1785 |
| cagr | -0.0280 |
| net_avg_win | 85.0045 |
| net_avg_loss | -103.9483 |
| avg_hold_time_bars | 39.0377 |
| exposure | 0.5181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
