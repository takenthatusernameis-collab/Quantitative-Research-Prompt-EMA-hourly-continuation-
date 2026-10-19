# EMA Hourly Continuation — AERO/USDT P26_89

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.6339 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -3.7917 |
| sortino_ratio | -1.3456 |
| max_drawdown | 0.8005 |
| cagr | -0.4719 |
| net_avg_win | 46.8861 |
| net_avg_loss | -65.1319 |
| avg_hold_time_bars | 9.7381 |
| exposure | 0.2789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
