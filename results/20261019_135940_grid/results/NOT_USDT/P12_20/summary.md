# EMA Hourly Continuation — NOT/USDT P12_20

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1491 |
| net_profit_factor | 0.3974 |
| net_win_rate | 0.4111 |
| gross_profit_factor | 0.8005 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -13.1701 |
| sortino_ratio | -7.3066 |
| max_drawdown | 0.9999 |
| cagr | -0.9783 |
| net_avg_win | 10.7551 |
| net_avg_loss | -18.8974 |
| avg_hold_time_bars | 2.0671 |
| exposure | 0.1448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
