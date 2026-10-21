# EMA Hourly Continuation — LUNC/USDT P21_26

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 146 |
| net_profit_factor | 0.6099 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -1.8809 |
| sortino_ratio | -0.3256 |
| max_drawdown | 0.3373 |
| cagr | -0.1392 |
| net_avg_win | 72.1068 |
| net_avg_loss | -103.0745 |
| avg_hold_time_bars | 4.2123 |
| exposure | 0.0280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
