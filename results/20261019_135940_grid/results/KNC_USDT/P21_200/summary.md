# EMA Hourly Continuation — KNC/USDT P21_200

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7470 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0805 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -1.8676 |
| sortino_ratio | -0.4926 |
| max_drawdown | 0.5159 |
| cagr | -0.2130 |
| net_avg_win | 72.9368 |
| net_avg_loss | -103.2842 |
| avg_hold_time_bars | 41.9298 |
| exposure | 0.6785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
