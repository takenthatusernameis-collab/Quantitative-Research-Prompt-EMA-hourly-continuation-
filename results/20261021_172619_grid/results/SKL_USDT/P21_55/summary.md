# EMA Hourly Continuation — SKL/USDT P21_55

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.6469 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8427 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -3.2385 |
| sortino_ratio | -1.0653 |
| max_drawdown | 0.7259 |
| cagr | -0.3868 |
| net_avg_win | 53.0960 |
| net_avg_loss | -69.0579 |
| avg_hold_time_bars | 8.1985 |
| exposure | 0.1990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
