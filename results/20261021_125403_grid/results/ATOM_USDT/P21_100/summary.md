# EMA Hourly Continuation — ATOM/USDT P21_100

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.8012 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0246 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.2911 |
| sortino_ratio | -0.3905 |
| max_drawdown | 0.4226 |
| cagr | -0.1658 |
| net_avg_win | 64.9310 |
| net_avg_loss | -85.1701 |
| avg_hold_time_bars | 19.7765 |
| exposure | 0.3982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
