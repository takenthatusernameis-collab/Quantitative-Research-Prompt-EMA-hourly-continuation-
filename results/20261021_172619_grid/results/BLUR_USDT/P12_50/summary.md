# EMA Hourly Continuation — BLUR/USDT P12_50

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.8060 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0446 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.6613 |
| sortino_ratio | -0.6146 |
| max_drawdown | 0.5831 |
| cagr | -0.2475 |
| net_avg_win | 62.0109 |
| net_avg_loss | -81.6977 |
| avg_hold_time_bars | 10.7432 |
| exposure | 0.3238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
