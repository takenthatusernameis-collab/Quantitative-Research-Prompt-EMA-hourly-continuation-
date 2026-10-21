# EMA Hourly Continuation — CRV/USDT P12_55

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.8126 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.5475 |
| sortino_ratio | -0.5348 |
| max_drawdown | 0.4882 |
| cagr | -0.2192 |
| net_avg_win | 68.2902 |
| net_avg_loss | -86.3850 |
| avg_hold_time_bars | 13.7672 |
| exposure | 0.3630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
