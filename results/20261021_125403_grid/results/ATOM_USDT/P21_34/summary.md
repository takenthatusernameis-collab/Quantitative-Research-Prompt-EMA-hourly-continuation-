# EMA Hourly Continuation — ATOM/USDT P21_34

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9249 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -2.3356 |
| sortino_ratio | -0.5408 |
| max_drawdown | 0.4767 |
| cagr | -0.2194 |
| net_avg_win | 62.0840 |
| net_avg_loss | -91.7951 |
| avg_hold_time_bars | 5.5654 |
| exposure | 0.0658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
