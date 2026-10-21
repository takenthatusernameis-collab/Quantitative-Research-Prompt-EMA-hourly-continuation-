# EMA Hourly Continuation — W/USDT P26_144

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 1.0176 |
| net_win_rate | 0.5462 |
| gross_profit_factor | 1.1990 |
| gross_win_rate | 0.5462 |
| sharpe_ratio | 0.1687 |
| sortino_ratio | 0.0476 |
| max_drawdown | 0.1233 |
| cagr | 0.0133 |
| net_avg_win | 94.1542 |
| net_avg_loss | -111.3573 |
| avg_hold_time_bars | 27.8496 |
| exposure | 0.4798 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
