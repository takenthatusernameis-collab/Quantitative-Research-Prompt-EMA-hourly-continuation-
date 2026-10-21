# EMA Hourly Continuation — AMP/USDT P12_100

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.5370 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.6825 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -4.7410 |
| sortino_ratio | -1.6571 |
| max_drawdown | 0.8590 |
| cagr | -0.5345 |
| net_avg_win | 39.4373 |
| net_avg_loss | -50.9202 |
| avg_hold_time_bars | 17.5644 |
| exposure | 0.4894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
