# EMA Hourly Continuation — CVX/USDT P26_55

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 888 |
| net_profit_factor | 0.4363 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.7254 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -6.8930 |
| sortino_ratio | -2.8995 |
| max_drawdown | 0.9714 |
| cagr | -0.7556 |
| net_avg_win | 19.3703 |
| net_avg_loss | -34.4503 |
| avg_hold_time_bars | 4.4876 |
| exposure | 0.1811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
