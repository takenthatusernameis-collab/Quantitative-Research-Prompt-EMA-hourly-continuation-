# EMA Hourly Continuation — NEO/USDT P55_100

**Symbol:** NEO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.6061 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.8821 |
| sortino_ratio | -0.7786 |
| max_drawdown | 0.6255 |
| cagr | -0.3012 |
| net_avg_win | 54.3465 |
| net_avg_loss | -79.7050 |
| avg_hold_time_bars | 7.7731 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
