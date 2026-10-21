# EMA Hourly Continuation — DYDX/USDT P12_50

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.7701 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9748 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -2.1266 |
| sortino_ratio | -0.7443 |
| max_drawdown | 0.6076 |
| cagr | -0.2898 |
| net_avg_win | 65.6920 |
| net_avg_loss | -81.9585 |
| avg_hold_time_bars | 12.6700 |
| exposure | 0.3455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
