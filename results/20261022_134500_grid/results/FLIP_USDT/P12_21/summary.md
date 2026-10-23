# EMA Hourly Continuation — FLIP/USDT P12_21

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.2698 |
| net_win_rate | 0.3356 |
| gross_profit_factor | 0.7686 |
| gross_win_rate | 0.3996 |
| sharpe_ratio | -13.8834 |
| sortino_ratio | -6.5541 |
| max_drawdown | 0.9998 |
| cagr | -0.9698 |
| net_avg_win | 10.5252 |
| net_avg_loss | -19.7019 |
| avg_hold_time_bars | 4.9436 |
| exposure | 0.2350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
