# EMA Hourly Continuation — UMA/USDT P55_100

**Symbol:** UMA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7612 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0908 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -1.6787 |
| sortino_ratio | -0.4721 |
| max_drawdown | 0.4431 |
| cagr | -0.1936 |
| net_avg_win | 66.8633 |
| net_avg_loss | -96.0485 |
| avg_hold_time_bars | 8.5354 |
| exposure | 0.1478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
