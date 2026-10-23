# EMA Hourly Continuation — CKB/USDT P21_100

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5987 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -4.8348 |
| sortino_ratio | -1.7684 |
| max_drawdown | 0.8867 |
| cagr | -0.5768 |
| net_avg_win | 42.7129 |
| net_avg_loss | -59.4196 |
| avg_hold_time_bars | 13.2029 |
| exposure | 0.4081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
