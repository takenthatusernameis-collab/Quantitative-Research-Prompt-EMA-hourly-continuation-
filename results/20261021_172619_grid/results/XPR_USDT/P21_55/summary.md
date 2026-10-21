# EMA Hourly Continuation — XPR/USDT P21_55

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7767 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0427 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.4796 |
| sortino_ratio | -0.3894 |
| max_drawdown | 0.4015 |
| cagr | -0.1635 |
| net_avg_win | 73.4987 |
| net_avg_loss | -98.6632 |
| avg_hold_time_bars | 11.8567 |
| exposure | 0.1805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
