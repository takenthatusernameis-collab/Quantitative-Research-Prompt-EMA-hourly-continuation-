# EMA Hourly Continuation — CGPT/USDT P89_200

**Symbol:** CGPT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.8631 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0777 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -0.7414 |
| sortino_ratio | -0.1715 |
| max_drawdown | 0.2389 |
| cagr | -0.0776 |
| net_avg_win | 86.3819 |
| net_avg_loss | -107.2842 |
| avg_hold_time_bars | 14.3475 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
