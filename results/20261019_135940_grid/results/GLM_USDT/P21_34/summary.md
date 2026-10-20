# EMA Hourly Continuation — GLM/USDT P21_34

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.3801 |
| net_win_rate | 0.4084 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -10.6417 |
| sortino_ratio | -4.9750 |
| max_drawdown | 0.9982 |
| cagr | -0.9193 |
| net_avg_win | 13.9406 |
| net_avg_loss | -25.3175 |
| avg_hold_time_bars | 3.3656 |
| exposure | 0.1645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
