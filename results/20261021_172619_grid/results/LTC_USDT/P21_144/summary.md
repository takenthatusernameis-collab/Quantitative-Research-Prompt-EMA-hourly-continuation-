# EMA Hourly Continuation — LTC/USDT P21_144

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.6216 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8151 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -2.7795 |
| sortino_ratio | -0.7463 |
| max_drawdown | 0.6004 |
| cagr | -0.2907 |
| net_avg_win | 58.9551 |
| net_avg_loss | -77.9133 |
| avg_hold_time_bars | 30.3838 |
| exposure | 0.4930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
