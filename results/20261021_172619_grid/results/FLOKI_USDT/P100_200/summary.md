# EMA Hourly Continuation — FLOKI/USDT P100_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.7032 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.8741 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -1.5291 |
| sortino_ratio | -0.3201 |
| max_drawdown | 0.3099 |
| cagr | -0.1373 |
| net_avg_win | 71.9993 |
| net_avg_loss | -91.6061 |
| avg_hold_time_bars | 18.8380 |
| exposure | 0.1850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
