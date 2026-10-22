# EMA Hourly Continuation — ILV/USDT P55_200

**Symbol:** ILV/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 1.0363 |
| net_win_rate | 0.5600 |
| gross_profit_factor | 1.2658 |
| gross_win_rate | 0.5600 |
| sharpe_ratio | 0.2374 |
| sortino_ratio | 0.0574 |
| max_drawdown | 0.0951 |
| cagr | 0.0195 |
| net_avg_win | 92.2695 |
| net_avg_loss | -113.3235 |
| avg_hold_time_bars | 30.2436 |
| exposure | 0.3780 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
