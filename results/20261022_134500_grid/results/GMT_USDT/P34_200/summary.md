# EMA Hourly Continuation — GMT/USDT P34_200

**Symbol:** GMT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.6692 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9463 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.0949 |
| sortino_ratio | -0.5600 |
| max_drawdown | 0.5041 |
| cagr | -0.2350 |
| net_avg_win | 55.6683 |
| net_avg_loss | -80.4679 |
| avg_hold_time_bars | 31.7459 |
| exposure | 0.5224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
