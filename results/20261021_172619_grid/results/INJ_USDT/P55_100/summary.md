# EMA Hourly Continuation — INJ/USDT P55_100

**Symbol:** INJ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7379 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.7016 |
| sortino_ratio | -0.4337 |
| max_drawdown | 0.4103 |
| cagr | -0.1807 |
| net_avg_win | 71.9853 |
| net_avg_loss | -91.6041 |
| avg_hold_time_bars | 7.5786 |
| exposure | 0.1095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
