# EMA Hourly Continuation — DEGEN/USDT P21_50

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.8041 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.6818 |
| sortino_ratio | -0.5283 |
| max_drawdown | 0.4952 |
| cagr | -0.2169 |
| net_avg_win | 79.0492 |
| net_avg_loss | -95.8859 |
| avg_hold_time_bars | 8.1328 |
| exposure | 0.1785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
