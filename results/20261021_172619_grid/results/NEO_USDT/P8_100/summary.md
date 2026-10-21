# EMA Hourly Continuation — NEO/USDT P8_100

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7750 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9625 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.5327 |
| sortino_ratio | -0.4311 |
| max_drawdown | 0.4486 |
| cagr | -0.1806 |
| net_avg_win | 70.6192 |
| net_avg_loss | -89.2619 |
| avg_hold_time_bars | 40.7603 |
| exposure | 0.7189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
