# EMA Hourly Continuation — SLP/USDT P21_55

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7403 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9953 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.9884 |
| sortino_ratio | -1.0267 |
| max_drawdown | 0.7483 |
| cagr | -0.3755 |
| net_avg_win | 71.6332 |
| net_avg_loss | -88.4294 |
| avg_hold_time_bars | 7.7837 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
