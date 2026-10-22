# EMA Hourly Continuation — RPL/USDT P8_89

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.8691 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0533 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.1306 |
| sortino_ratio | -0.3807 |
| max_drawdown | 0.4881 |
| cagr | -0.1639 |
| net_avg_win | 85.2740 |
| net_avg_loss | -102.4601 |
| avg_hold_time_bars | 25.0325 |
| exposure | 0.6276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
