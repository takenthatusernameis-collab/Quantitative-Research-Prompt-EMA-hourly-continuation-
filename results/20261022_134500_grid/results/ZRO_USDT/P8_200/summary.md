# EMA Hourly Continuation — ZRO/USDT P8_200

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.8210 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.1676 |
| sortino_ratio | -0.3282 |
| max_drawdown | 0.3355 |
| cagr | -0.1438 |
| net_avg_win | 75.7479 |
| net_avg_loss | -95.3717 |
| avg_hold_time_bars | 44.6713 |
| exposure | 0.7915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
