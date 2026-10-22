# EMA Hourly Continuation — ELON/USDT P8_12

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.6889 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6839 |
| sortino_ratio | -0.3562 |
| max_drawdown | 0.3689 |
| cagr | -0.1496 |
| net_avg_win | 68.5645 |
| net_avg_loss | -99.5278 |
| avg_hold_time_bars | 5.5648 |
| exposure | 0.0546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
