# EMA Hourly Continuation — IMX/USDT P50_100

**Symbol:** IMX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5382 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -4.7220 |
| sortino_ratio | -1.6810 |
| max_drawdown | 0.8778 |
| cagr | -0.5596 |
| net_avg_win | 33.8322 |
| net_avg_loss | -55.1603 |
| avg_hold_time_bars | 5.3339 |
| exposure | 0.1554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
