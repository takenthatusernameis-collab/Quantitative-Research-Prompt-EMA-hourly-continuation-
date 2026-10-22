# EMA Hourly Continuation — ADA/USDT P20_55

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.4447 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8824 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -6.8909 |
| sortino_ratio | -2.9623 |
| max_drawdown | 0.9748 |
| cagr | -0.7652 |
| net_avg_win | 18.2190 |
| net_avg_loss | -34.8608 |
| avg_hold_time_bars | 5.4619 |
| exposure | 0.2311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
