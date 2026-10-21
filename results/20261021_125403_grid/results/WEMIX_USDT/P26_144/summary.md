# EMA Hourly Continuation — WEMIX/USDT P26_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.5478 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.6844 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -3.8656 |
| sortino_ratio | -1.0546 |
| max_drawdown | 0.7129 |
| cagr | -0.3873 |
| net_avg_win | 57.1688 |
| net_avg_loss | -69.5681 |
| avg_hold_time_bars | 29.1413 |
| exposure | 0.4967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
