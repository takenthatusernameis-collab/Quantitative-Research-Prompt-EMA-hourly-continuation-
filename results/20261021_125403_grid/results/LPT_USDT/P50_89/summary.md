# EMA Hourly Continuation — LPT/USDT P50_89

**Symbol:** LPT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.5669 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.7609 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -3.5622 |
| sortino_ratio | -0.9885 |
| max_drawdown | 0.6890 |
| cagr | -0.3675 |
| net_avg_win | 54.2249 |
| net_avg_loss | -73.0625 |
| avg_hold_time_bars | 7.3727 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
