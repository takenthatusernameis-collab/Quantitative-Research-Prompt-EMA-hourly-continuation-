# EMA Hourly Continuation — XTZ/USDT P12_200

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.8271 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -0.8855 |
| sortino_ratio | -0.1982 |
| max_drawdown | 0.2231 |
| cagr | -0.0884 |
| net_avg_win | 80.6272 |
| net_avg_loss | -99.0982 |
| avg_hold_time_bars | 71.3074 |
| exposure | 0.7909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
