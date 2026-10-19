# EMA Hourly Continuation — APE/USDT P21_26

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.1456 |
| net_win_rate | 0.3362 |
| gross_profit_factor | 0.5425 |
| gross_win_rate | 0.3871 |
| sharpe_ratio | -15.1885 |
| sortino_ratio | -7.6026 |
| max_drawdown | 1.0000 |
| cagr | -0.9838 |
| net_avg_win | 4.3019 |
| net_avg_loss | -14.9658 |
| avg_hold_time_bars | 1.7419 |
| exposure | 0.0933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
