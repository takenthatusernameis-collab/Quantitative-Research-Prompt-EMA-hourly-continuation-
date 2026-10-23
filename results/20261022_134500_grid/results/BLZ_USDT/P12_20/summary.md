# EMA Hourly Continuation — BLZ/USDT P12_20

**Symbol:** BLZ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1456 |
| net_profit_factor | 0.3277 |
| net_win_rate | 0.3620 |
| gross_profit_factor | 0.9039 |
| gross_win_rate | 0.4018 |
| sharpe_ratio | -14.5000 |
| sortino_ratio | -7.8917 |
| max_drawdown | 1.0000 |
| cagr | -0.9826 |
| net_avg_win | 9.2505 |
| net_avg_loss | -16.0115 |
| avg_hold_time_bars | 3.0927 |
| exposure | 0.2038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
