# EMA Hourly Continuation — LTC/USDT P12_50

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.3602 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -9.4568 |
| sortino_ratio | -4.4071 |
| max_drawdown | 0.9967 |
| cagr | -0.8960 |
| net_avg_win | 11.6660 |
| net_avg_loss | -25.1654 |
| avg_hold_time_bars | 6.3582 |
| exposure | 0.3179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
