# EMA Hourly Continuation — CRV/USDT P8_34

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1387 |
| net_profit_factor | 0.5685 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9613 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -6.9623 |
| sortino_ratio | -3.6397 |
| max_drawdown | 0.9889 |
| cagr | -0.8303 |
| net_avg_win | 19.6987 |
| net_avg_loss | -31.5489 |
| avg_hold_time_bars | 5.0332 |
| exposure | 0.3173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
