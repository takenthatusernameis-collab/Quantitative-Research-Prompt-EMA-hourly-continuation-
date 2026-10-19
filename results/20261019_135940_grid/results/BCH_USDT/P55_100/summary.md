# EMA Hourly Continuation — BCH/USDT P55_100

**Symbol:** BCH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.4446 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8818 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -6.6957 |
| sortino_ratio | -2.4186 |
| max_drawdown | 0.9517 |
| cagr | -0.6978 |
| net_avg_win | 26.1416 |
| net_avg_loss | -47.9329 |
| avg_hold_time_bars | 5.0201 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
