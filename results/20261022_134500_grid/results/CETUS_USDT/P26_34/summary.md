# EMA Hourly Continuation — CETUS/USDT P26_34

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.3877 |
| net_win_rate | 0.3854 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -11.6014 |
| sortino_ratio | -5.4542 |
| max_drawdown | 0.9991 |
| cagr | -0.9382 |
| net_avg_win | 15.1709 |
| net_avg_loss | -24.5374 |
| avg_hold_time_bars | 2.2865 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
