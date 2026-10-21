# EMA Hourly Continuation — AERO/USDT P34_200

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.9221 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.0668 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -0.3896 |
| sortino_ratio | -0.0909 |
| max_drawdown | 0.2034 |
| cagr | -0.0441 |
| net_avg_win | 93.3250 |
| net_avg_loss | -108.3765 |
| avg_hold_time_bars | 41.4563 |
| exposure | 0.4956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
