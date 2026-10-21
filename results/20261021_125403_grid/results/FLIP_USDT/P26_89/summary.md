# EMA Hourly Continuation — FLIP/USDT P26_89

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6583 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -2.4337 |
| sortino_ratio | -0.6557 |
| max_drawdown | 0.5478 |
| cagr | -0.2606 |
| net_avg_win | 59.5228 |
| net_avg_loss | -83.1700 |
| avg_hold_time_bars | 19.3621 |
| exposure | 0.3160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
