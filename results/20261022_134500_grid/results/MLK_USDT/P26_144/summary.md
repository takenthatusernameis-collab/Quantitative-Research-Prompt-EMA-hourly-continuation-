# EMA Hourly Continuation — MLK/USDT P26_144

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.3619 |
| net_win_rate | 0.3284 |
| gross_profit_factor | 0.5894 |
| gross_win_rate | 0.3311 |
| sharpe_ratio | -9.3777 |
| sortino_ratio | -3.6141 |
| max_drawdown | 0.9888 |
| cagr | -0.8303 |
| net_avg_win | 22.9837 |
| net_avg_loss | -31.0502 |
| avg_hold_time_bars | 13.0067 |
| exposure | 0.4373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
