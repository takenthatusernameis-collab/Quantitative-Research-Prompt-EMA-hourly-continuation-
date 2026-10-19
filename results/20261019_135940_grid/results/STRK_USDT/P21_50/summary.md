# EMA Hourly Continuation — STRK/USDT P21_50

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.9398 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -6.1237 |
| sortino_ratio | -2.7191 |
| max_drawdown | 0.9616 |
| cagr | -0.7258 |
| net_avg_win | 26.3290 |
| net_avg_loss | -41.3059 |
| avg_hold_time_bars | 4.4230 |
| exposure | 0.1972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
