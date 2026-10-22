# EMA Hourly Continuation — XRP/USDT P8_26

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1580 |
| net_profit_factor | 0.2498 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.8326 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -13.5782 |
| sortino_ratio | -7.6068 |
| max_drawdown | 1.0000 |
| cagr | -0.9837 |
| net_avg_win | 5.0290 |
| net_avg_loss | -14.5195 |
| avg_hold_time_bars | 3.3633 |
| exposure | 0.2415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
