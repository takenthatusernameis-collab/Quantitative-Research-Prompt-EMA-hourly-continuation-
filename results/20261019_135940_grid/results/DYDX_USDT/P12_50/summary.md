# EMA Hourly Continuation — DYDX/USDT P12_50

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.5996 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -5.5141 |
| sortino_ratio | -2.4242 |
| max_drawdown | 0.9486 |
| cagr | -0.6881 |
| net_avg_win | 31.0797 |
| net_avg_loss | -45.2801 |
| avg_hold_time_bars | 8.4233 |
| exposure | 0.3745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
