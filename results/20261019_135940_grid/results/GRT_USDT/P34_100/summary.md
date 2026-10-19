# EMA Hourly Continuation — GRT/USDT P34_100

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5834 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9122 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -3.9804 |
| sortino_ratio | -1.4159 |
| max_drawdown | 0.8272 |
| cagr | -0.4902 |
| net_avg_win | 37.4023 |
| net_avg_loss | -59.4465 |
| avg_hold_time_bars | 9.2170 |
| exposure | 0.2653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
