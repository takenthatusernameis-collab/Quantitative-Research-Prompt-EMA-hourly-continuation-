# EMA Hourly Continuation — RAY/USDT P20_21

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 166 |
| net_profit_factor | 0.5852 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8410 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -2.2600 |
| sortino_ratio | -0.4154 |
| max_drawdown | 0.4038 |
| cagr | -0.1764 |
| net_avg_win | 72.5662 |
| net_avg_loss | -102.1941 |
| avg_hold_time_bars | 4.7831 |
| exposure | 0.0361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
