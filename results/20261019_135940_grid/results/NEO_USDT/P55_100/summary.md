# EMA Hourly Continuation — NEO/USDT P55_100

**Symbol:** NEO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.3981 |
| net_win_rate | 0.4233 |
| gross_profit_factor | 0.7981 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -6.8913 |
| sortino_ratio | -2.5086 |
| max_drawdown | 0.9536 |
| cagr | -0.7035 |
| net_avg_win | 22.8308 |
| net_avg_loss | -42.0984 |
| avg_hold_time_bars | 5.0721 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
