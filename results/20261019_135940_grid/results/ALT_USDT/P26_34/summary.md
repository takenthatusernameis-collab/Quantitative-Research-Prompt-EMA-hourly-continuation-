# EMA Hourly Continuation — ALT/USDT P26_34

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 945 |
| net_profit_factor | 0.3186 |
| net_win_rate | 0.4116 |
| gross_profit_factor | 0.7356 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -9.7349 |
| sortino_ratio | -4.2306 |
| max_drawdown | 0.9959 |
| cagr | -0.8865 |
| net_avg_win | 11.9707 |
| net_avg_loss | -26.2846 |
| avg_hold_time_bars | 3.2360 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
