# EMA Hourly Continuation — SKY/USDT P8_55

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.7556 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -2.6003 |
| sortino_ratio | -1.0212 |
| max_drawdown | 0.6789 |
| cagr | -0.3757 |
| net_avg_win | 62.5204 |
| net_avg_loss | -81.6744 |
| avg_hold_time_bars | 12.7305 |
| exposure | 0.4373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
