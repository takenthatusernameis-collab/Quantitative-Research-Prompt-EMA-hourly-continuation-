# EMA Hourly Continuation — IMX/USDT P12_50

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.8385 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0464 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.2361 |
| sortino_ratio | -0.4478 |
| max_drawdown | 0.4470 |
| cagr | -0.1889 |
| net_avg_win | 64.7200 |
| net_avg_loss | -82.4525 |
| avg_hold_time_bars | 11.1727 |
| exposure | 0.3221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
