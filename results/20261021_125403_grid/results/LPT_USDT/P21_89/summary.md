# EMA Hourly Continuation — LPT/USDT P21_89

**Symbol:** LPT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6864 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -3.0811 |
| sortino_ratio | -1.0159 |
| max_drawdown | 0.7080 |
| cagr | -0.3754 |
| net_avg_win | 61.4451 |
| net_avg_loss | -75.4607 |
| avg_hold_time_bars | 13.7389 |
| exposure | 0.3372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
