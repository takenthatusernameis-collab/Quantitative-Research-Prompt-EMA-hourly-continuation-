# EMA Hourly Continuation — IO/USDT P12_20

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1420 |
| net_profit_factor | 0.4526 |
| net_win_rate | 0.4218 |
| gross_profit_factor | 0.8399 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -11.5721 |
| sortino_ratio | -6.3573 |
| max_drawdown | 0.9995 |
| cagr | -0.9595 |
| net_avg_win | 13.7967 |
| net_avg_loss | -22.2400 |
| avg_hold_time_bars | 2.0915 |
| exposure | 0.1438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
