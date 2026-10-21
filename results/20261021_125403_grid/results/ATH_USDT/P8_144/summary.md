# EMA Hourly Continuation — ATH/USDT P8_144

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 1.0173 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.1820 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | 0.1575 |
| sortino_ratio | 0.0421 |
| max_drawdown | 0.0993 |
| cagr | 0.0116 |
| net_avg_win | 93.1279 |
| net_avg_loss | -109.8514 |
| avg_hold_time_bars | 49.4044 |
| exposure | 0.7639 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
