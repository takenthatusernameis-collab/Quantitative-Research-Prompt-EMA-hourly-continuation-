# EMA Hourly Continuation — NEO/USDT P20_100

**Symbol:** NEO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6719 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.5973 |
| sortino_ratio | -0.7941 |
| max_drawdown | 0.6106 |
| cagr | -0.3044 |
| net_avg_win | 56.1791 |
| net_avg_loss | -75.6377 |
| avg_hold_time_bars | 21.0065 |
| exposure | 0.4383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
