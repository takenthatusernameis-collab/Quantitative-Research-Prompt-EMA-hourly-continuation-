# EMA Hourly Continuation — GMX/USDT P89_144

**Symbol:** GMX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.5563 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.7772 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -3.4324 |
| sortino_ratio | -0.9265 |
| max_drawdown | 0.6583 |
| cagr | -0.3479 |
| net_avg_win | 52.5605 |
| net_avg_loss | -73.4386 |
| avg_hold_time_bars | 6.6323 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
