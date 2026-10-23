# EMA Hourly Continuation — AURORA/USDT P12_89

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.5812 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8791 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -4.7249 |
| sortino_ratio | -1.6314 |
| max_drawdown | 0.8672 |
| cagr | -0.5525 |
| net_avg_win | 43.6104 |
| net_avg_loss | -61.4502 |
| avg_hold_time_bars | 18.8010 |
| exposure | 0.5239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
