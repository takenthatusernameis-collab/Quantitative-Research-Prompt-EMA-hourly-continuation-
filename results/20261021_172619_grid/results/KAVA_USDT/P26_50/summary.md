# EMA Hourly Continuation — KAVA/USDT P26_50

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5531 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -4.6802 |
| sortino_ratio | -1.4733 |
| max_drawdown | 0.8275 |
| cagr | -0.4987 |
| net_avg_win | 47.1721 |
| net_avg_loss | -68.4882 |
| avg_hold_time_bars | 6.0289 |
| exposure | 0.1329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
