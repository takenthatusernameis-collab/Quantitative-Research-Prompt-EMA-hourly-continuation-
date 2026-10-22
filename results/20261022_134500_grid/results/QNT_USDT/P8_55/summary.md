# EMA Hourly Continuation — QNT/USDT P8_55

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1299 |
| net_profit_factor | 0.4598 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8392 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -8.4650 |
| sortino_ratio | -4.2761 |
| max_drawdown | 0.9952 |
| cagr | -0.8799 |
| net_avg_win | 14.6014 |
| net_avg_loss | -25.6189 |
| avg_hold_time_bars | 7.1378 |
| exposure | 0.4215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
