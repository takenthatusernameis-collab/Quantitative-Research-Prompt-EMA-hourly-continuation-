# EMA Hourly Continuation — CKB/USDT P89_200

**Symbol:** CKB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7074 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -1.7923 |
| sortino_ratio | -0.4460 |
| max_drawdown | 0.4024 |
| cagr | -0.1853 |
| net_avg_win | 66.6270 |
| net_avg_loss | -87.0325 |
| avg_hold_time_bars | 15.4211 |
| exposure | 0.2131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
