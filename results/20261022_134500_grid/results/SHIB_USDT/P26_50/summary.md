# EMA Hourly Continuation — SHIB/USDT P26_50

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.4120 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8816 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -9.6321 |
| sortino_ratio | -4.2854 |
| max_drawdown | 0.9956 |
| cagr | -0.8826 |
| net_avg_win | 17.1365 |
| net_avg_loss | -30.1219 |
| avg_hold_time_bars | 3.2642 |
| exposure | 0.1438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
