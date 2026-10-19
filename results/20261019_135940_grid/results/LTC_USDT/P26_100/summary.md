# EMA Hourly Continuation — LTC/USDT P26_100

**Symbol:** LTC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.4231 |
| net_win_rate | 0.4196 |
| gross_profit_factor | 0.8483 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -6.8327 |
| sortino_ratio | -2.5001 |
| max_drawdown | 0.9563 |
| cagr | -0.7075 |
| net_avg_win | 24.8223 |
| net_avg_loss | -42.4198 |
| avg_hold_time_bars | 11.0342 |
| exposure | 0.3370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
