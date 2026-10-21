# EMA Hourly Continuation — AXS/USDT P12_55

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.7967 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0378 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -1.7770 |
| sortino_ratio | -0.6126 |
| max_drawdown | 0.5312 |
| cagr | -0.2456 |
| net_avg_win | 67.8349 |
| net_avg_loss | -87.8324 |
| avg_hold_time_bars | 13.3921 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
