# EMA Hourly Continuation — CTC/USDT P8_34

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1346 |
| net_profit_factor | 0.4648 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -9.0352 |
| sortino_ratio | -4.6547 |
| max_drawdown | 0.9972 |
| cagr | -0.9019 |
| net_avg_win | 14.4098 |
| net_avg_loss | -25.0079 |
| avg_hold_time_bars | 6.0513 |
| exposure | 0.3702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
