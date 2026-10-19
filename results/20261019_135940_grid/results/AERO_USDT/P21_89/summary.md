# EMA Hourly Continuation — AERO/USDT P21_89

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.9309 |
| sortino_ratio | -1.0482 |
| max_drawdown | 0.7151 |
| cagr | -0.3890 |
| net_avg_win | 54.0192 |
| net_avg_loss | -73.7608 |
| avg_hold_time_bars | 11.9370 |
| exposure | 0.3445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
