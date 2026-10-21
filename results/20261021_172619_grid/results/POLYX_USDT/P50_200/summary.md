# EMA Hourly Continuation — POLYX/USDT P50_200

**Symbol:** POLYX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.7544 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -1.4951 |
| sortino_ratio | -0.3557 |
| max_drawdown | 0.3511 |
| cagr | -0.1517 |
| net_avg_win | 77.0140 |
| net_avg_loss | -96.3694 |
| avg_hold_time_bars | 31.4784 |
| exposure | 0.3978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
