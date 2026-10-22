# EMA Hourly Continuation — HBAR/USDT P144_200

**Symbol:** HBAR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.5187 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 1.0127 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -4.3350 |
| sortino_ratio | -1.2050 |
| max_drawdown | 0.7866 |
| cagr | -0.4516 |
| net_avg_win | 44.3989 |
| net_avg_loss | -81.3013 |
| avg_hold_time_bars | 4.5361 |
| exposure | 0.0800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
