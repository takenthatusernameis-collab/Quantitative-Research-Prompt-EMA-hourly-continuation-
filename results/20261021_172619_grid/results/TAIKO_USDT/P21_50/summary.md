# EMA Hourly Continuation — TAIKO/USDT P21_50

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.6999 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.4168 |
| sortino_ratio | -0.7654 |
| max_drawdown | 0.6043 |
| cagr | -0.2953 |
| net_avg_win | 57.2515 |
| net_avg_loss | -81.0961 |
| avg_hold_time_bars | 8.2576 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
