# EMA Hourly Continuation — CPOOL/USDT P8_21

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1589 |
| net_profit_factor | 0.5638 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8878 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -10.0490 |
| sortino_ratio | -5.6125 |
| max_drawdown | 0.9991 |
| cagr | -0.9384 |
| net_avg_win | 18.7391 |
| net_avg_loss | -25.4468 |
| avg_hold_time_bars | 3.1410 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
