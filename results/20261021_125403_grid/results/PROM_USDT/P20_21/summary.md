# EMA Hourly Continuation — PROM/USDT P20_21

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.3830 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.6452 |
| gross_win_rate | 0.3991 |
| sharpe_ratio | -4.1036 |
| sortino_ratio | -0.8680 |
| max_drawdown | 0.6505 |
| cagr | -0.3370 |
| net_avg_win | 47.0073 |
| net_avg_loss | -78.4435 |
| avg_hold_time_bars | 4.8349 |
| exposure | 0.0479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
