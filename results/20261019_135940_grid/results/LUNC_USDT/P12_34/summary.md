# EMA Hourly Continuation — LUNC/USDT P12_34

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1399 |
| net_profit_factor | 0.3208 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.7294 |
| gross_win_rate | 0.4139 |
| sharpe_ratio | -12.2556 |
| sortino_ratio | -6.5270 |
| max_drawdown | 0.9997 |
| cagr | -0.9605 |
| net_avg_win | 8.6153 |
| net_avg_loss | -17.2952 |
| avg_hold_time_bars | 3.6033 |
| exposure | 0.2291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
