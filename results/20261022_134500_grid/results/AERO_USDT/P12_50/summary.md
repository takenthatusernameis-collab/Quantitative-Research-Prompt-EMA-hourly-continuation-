# EMA Hourly Continuation — AERO/USDT P12_50

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.5728 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9020 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -5.2755 |
| sortino_ratio | -2.3503 |
| max_drawdown | 0.9468 |
| cagr | -0.6836 |
| net_avg_win | 26.1113 |
| net_avg_loss | -41.6349 |
| avg_hold_time_bars | 7.2904 |
| exposure | 0.3367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
