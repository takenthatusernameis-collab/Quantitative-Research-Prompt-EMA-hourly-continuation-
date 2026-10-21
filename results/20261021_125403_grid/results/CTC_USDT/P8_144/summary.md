# EMA Hourly Continuation — CTC/USDT P8_144

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.8322 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0249 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.1323 |
| sortino_ratio | -0.3314 |
| max_drawdown | 0.4677 |
| cagr | -0.1445 |
| net_avg_win | 75.4575 |
| net_avg_loss | -94.2161 |
| avg_hold_time_bars | 37.7919 |
| exposure | 0.7180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
