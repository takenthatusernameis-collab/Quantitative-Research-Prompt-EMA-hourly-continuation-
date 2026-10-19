# EMA Hourly Continuation — JTO/USDT P8_20

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1694 |
| net_profit_factor | 0.3890 |
| net_win_rate | 0.4233 |
| gross_profit_factor | 0.7378 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -11.0983 |
| sortino_ratio | -6.4079 |
| max_drawdown | 0.9997 |
| cagr | -0.9588 |
| net_avg_win | 8.8750 |
| net_avg_loss | -16.7452 |
| avg_hold_time_bars | 3.0242 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
