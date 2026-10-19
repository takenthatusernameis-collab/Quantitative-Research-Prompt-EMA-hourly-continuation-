# EMA Hourly Continuation — NEO/USDT P50_89

**Symbol:** NEO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.3935 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.7953 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -7.0213 |
| sortino_ratio | -2.6525 |
| max_drawdown | 0.9630 |
| cagr | -0.7268 |
| net_avg_win | 20.2526 |
| net_avg_loss | -39.4359 |
| avg_hold_time_bars | 4.5437 |
| exposure | 0.1466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
