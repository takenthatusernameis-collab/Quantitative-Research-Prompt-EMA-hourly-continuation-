# EMA Hourly Continuation — DYDX/USDT P12_200

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.7222 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 0.9963 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.6185 |
| sortino_ratio | -0.3780 |
| max_drawdown | 0.3937 |
| cagr | -0.1649 |
| net_avg_win | 68.0855 |
| net_avg_loss | -95.6454 |
| avg_hold_time_bars | 64.9928 |
| exposure | 0.8154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
