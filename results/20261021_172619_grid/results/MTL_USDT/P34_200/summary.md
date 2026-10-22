# EMA Hourly Continuation — MTL/USDT P34_200

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7305 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.7613 |
| sortino_ratio | -0.4355 |
| max_drawdown | 0.4132 |
| cagr | -0.1827 |
| net_avg_win | 73.5235 |
| net_avg_loss | -94.8462 |
| avg_hold_time_bars | 39.0627 |
| exposure | 0.5356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
