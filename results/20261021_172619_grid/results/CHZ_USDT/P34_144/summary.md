# EMA Hourly Continuation — CHZ/USDT P34_144

**Symbol:** CHZ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8909 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1139 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -0.6334 |
| sortino_ratio | -0.1722 |
| max_drawdown | 0.3279 |
| cagr | -0.0795 |
| net_avg_win | 81.6211 |
| net_avg_loss | -102.5239 |
| avg_hold_time_bars | 25.1489 |
| exposure | 0.4070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
