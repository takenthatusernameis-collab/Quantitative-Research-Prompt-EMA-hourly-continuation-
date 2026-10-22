# EMA Hourly Continuation — ONDO/USDT P21_26

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1186 |
| net_profit_factor | 0.2838 |
| net_win_rate | 0.3702 |
| gross_profit_factor | 0.7166 |
| gross_win_rate | 0.4047 |
| sharpe_ratio | -13.8413 |
| sortino_ratio | -6.9226 |
| max_drawdown | 0.9999 |
| cagr | -0.9738 |
| net_avg_win | 9.0238 |
| net_avg_loss | -18.6886 |
| avg_hold_time_bars | 1.7218 |
| exposure | 0.0928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
