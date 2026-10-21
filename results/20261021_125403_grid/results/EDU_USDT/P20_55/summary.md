# EMA Hourly Continuation — EDU/USDT P20_55

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6300 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8245 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -3.2430 |
| sortino_ratio | -1.1513 |
| max_drawdown | 0.7446 |
| cagr | -0.4109 |
| net_avg_win | 43.2492 |
| net_avg_loss | -59.6103 |
| avg_hold_time_bars | 7.8109 |
| exposure | 0.2206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
