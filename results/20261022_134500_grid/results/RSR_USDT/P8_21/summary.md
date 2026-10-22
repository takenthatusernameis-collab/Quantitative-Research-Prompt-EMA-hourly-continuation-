# EMA Hourly Continuation — RSR/USDT P8_21

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1655 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.9201 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -10.0281 |
| sortino_ratio | -5.7317 |
| max_drawdown | 0.9992 |
| cagr | -0.9415 |
| net_avg_win | 13.1184 |
| net_avg_loss | -21.6055 |
| avg_hold_time_bars | 3.1202 |
| exposure | 0.2347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
