# EMA Hourly Continuation — INJ/USDT P26_100

**Symbol:** INJ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8306 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.3765 |
| sortino_ratio | -0.4240 |
| max_drawdown | 0.4621 |
| cagr | -0.1787 |
| net_avg_win | 82.7766 |
| net_avg_loss | -99.2311 |
| avg_hold_time_bars | 13.5292 |
| exposure | 0.2847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
