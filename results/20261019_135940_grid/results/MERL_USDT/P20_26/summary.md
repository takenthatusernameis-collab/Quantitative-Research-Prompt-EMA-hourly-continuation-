# EMA Hourly Continuation — MERL/USDT P20_26

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1218 |
| net_profit_factor | 0.3184 |
| net_win_rate | 0.3851 |
| gross_profit_factor | 0.6131 |
| gross_win_rate | 0.4122 |
| sharpe_ratio | -11.6243 |
| sortino_ratio | -5.7450 |
| max_drawdown | 0.9993 |
| cagr | -0.9465 |
| net_avg_win | 9.9522 |
| net_avg_loss | -19.5742 |
| avg_hold_time_bars | 2.2044 |
| exposure | 0.1224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
