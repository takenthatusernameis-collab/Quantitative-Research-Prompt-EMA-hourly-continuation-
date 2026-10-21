# EMA Hourly Continuation — REZ/USDT P50_100

**Symbol:** REZ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.9623 |
| net_win_rate | 0.5510 |
| gross_profit_factor | 1.2111 |
| gross_win_rate | 0.5510 |
| sharpe_ratio | -0.1631 |
| sortino_ratio | -0.0472 |
| max_drawdown | 0.2921 |
| cagr | -0.0281 |
| net_avg_win | 80.4699 |
| net_avg_loss | -102.6295 |
| avg_hold_time_bars | 9.7117 |
| exposure | 0.1756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
