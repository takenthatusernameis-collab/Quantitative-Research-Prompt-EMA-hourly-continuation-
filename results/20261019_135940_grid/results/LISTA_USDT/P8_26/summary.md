# EMA Hourly Continuation — LISTA/USDT P8_26

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1272 |
| net_profit_factor | 0.6203 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 1.0134 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -7.6258 |
| sortino_ratio | -3.9767 |
| max_drawdown | 0.9889 |
| cagr | -0.8515 |
| net_avg_win | 28.2758 |
| net_avg_loss | -37.1311 |
| avg_hold_time_bars | 4.7272 |
| exposure | 0.2940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
