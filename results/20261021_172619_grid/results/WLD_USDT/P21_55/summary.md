# EMA Hourly Continuation — WLD/USDT P21_55

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7942 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -1.4606 |
| sortino_ratio | -0.4407 |
| max_drawdown | 0.4318 |
| cagr | -0.1844 |
| net_avg_win | 69.9627 |
| net_avg_loss | -87.2989 |
| avg_hold_time_bars | 10.3806 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
