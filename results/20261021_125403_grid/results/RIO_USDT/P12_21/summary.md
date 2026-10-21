# EMA Hourly Continuation — RIO/USDT P12_21

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.7773 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9408 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -1.3626 |
| sortino_ratio | -0.3150 |
| max_drawdown | 0.3516 |
| cagr | -0.1354 |
| net_avg_win | 84.7269 |
| net_avg_loss | -100.9312 |
| avg_hold_time_bars | 5.5962 |
| exposure | 0.0668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
