# EMA Hourly Continuation — CKB/USDT P8_12

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6591 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.4268 |
| sortino_ratio | -0.6004 |
| max_drawdown | 0.5541 |
| cagr | -0.2414 |
| net_avg_win | 66.7205 |
| net_avg_loss | -95.9363 |
| avg_hold_time_bars | 4.6913 |
| exposure | 0.0635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
