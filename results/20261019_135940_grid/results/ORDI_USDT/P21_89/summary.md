# EMA Hourly Continuation — ORDI/USDT P21_89

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.6340 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -4.4851 |
| sortino_ratio | -1.7268 |
| max_drawdown | 0.8777 |
| cagr | -0.5572 |
| net_avg_win | 43.8520 |
| net_avg_loss | -59.4800 |
| avg_hold_time_bars | 9.9005 |
| exposure | 0.3348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
