# EMA Hourly Continuation — HNT/USDT P8_21

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.8247 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -3.7919 |
| sortino_ratio | -1.2378 |
| max_drawdown | 0.7637 |
| cagr | -0.4341 |
| net_avg_win | 53.5670 |
| net_avg_loss | -68.3250 |
| avg_hold_time_bars | 6.7002 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
