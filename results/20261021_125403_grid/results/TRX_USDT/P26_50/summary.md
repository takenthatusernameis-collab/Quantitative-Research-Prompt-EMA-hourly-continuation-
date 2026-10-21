# EMA Hourly Continuation — TRX/USDT P26_50

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.3942 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -4.8814 |
| sortino_ratio | -1.2718 |
| max_drawdown | 0.7745 |
| cagr | -0.4396 |
| net_avg_win | 33.4758 |
| net_avg_loss | -77.1470 |
| avg_hold_time_bars | 7.3067 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
