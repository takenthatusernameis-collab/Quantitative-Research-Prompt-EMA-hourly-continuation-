# EMA Hourly Continuation — CFG/USDT P12_55

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 848 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8594 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -5.1250 |
| sortino_ratio | -2.1075 |
| max_drawdown | 0.9228 |
| cagr | -0.6320 |
| net_avg_win | 26.9291 |
| net_avg_loss | -41.9392 |
| avg_hold_time_bars | 13.4139 |
| exposure | 0.5170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
