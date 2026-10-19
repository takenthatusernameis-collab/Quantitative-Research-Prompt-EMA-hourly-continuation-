# EMA Hourly Continuation — CRV/USDT P20_50

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.5862 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 1.0211 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -5.8852 |
| sortino_ratio | -2.6113 |
| max_drawdown | 0.9591 |
| cagr | -0.7173 |
| net_avg_win | 28.4544 |
| net_avg_loss | -45.1340 |
| avg_hold_time_bars | 4.3202 |
| exposure | 0.1944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
