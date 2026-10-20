# EMA Hourly Continuation — ENJ/USDT P55_100

**Symbol:** ENJ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -4.7469 |
| sortino_ratio | -1.6599 |
| max_drawdown | 0.8661 |
| cagr | -0.5484 |
| net_avg_win | 35.6043 |
| net_avg_loss | -59.1600 |
| avg_hold_time_bars | 5.7225 |
| exposure | 0.1584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
