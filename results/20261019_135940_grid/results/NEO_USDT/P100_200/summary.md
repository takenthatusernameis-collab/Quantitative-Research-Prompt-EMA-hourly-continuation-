# EMA Hourly Continuation — NEO/USDT P100_200

**Symbol:** NEO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.3930 |
| net_win_rate | 0.4254 |
| gross_profit_factor | 0.7349 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -5.4483 |
| sortino_ratio | -1.6313 |
| max_drawdown | 0.8668 |
| cagr | -0.5503 |
| net_avg_win | 29.3409 |
| net_avg_loss | -55.2713 |
| avg_hold_time_bars | 7.2806 |
| exposure | 0.1486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
