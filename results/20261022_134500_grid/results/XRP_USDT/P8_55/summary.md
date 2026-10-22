# EMA Hourly Continuation — XRP/USDT P8_55

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1169 |
| net_profit_factor | 0.3926 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.8842 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -9.4000 |
| sortino_ratio | -4.4956 |
| max_drawdown | 0.9971 |
| cagr | -0.9016 |
| net_avg_win | 12.7095 |
| net_avg_loss | -24.7947 |
| avg_hold_time_bars | 8.1129 |
| exposure | 0.4311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
