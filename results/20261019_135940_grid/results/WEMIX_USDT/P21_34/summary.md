# EMA Hourly Continuation — WEMIX/USDT P21_34

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1631 |
| net_profit_factor | 0.1237 |
| net_win_rate | 0.2594 |
| gross_profit_factor | 0.3414 |
| gross_win_rate | 0.2918 |
| sharpe_ratio | -21.0108 |
| sortino_ratio | -12.5441 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 3.3365 |
| net_avg_loss | -9.4465 |
| avg_hold_time_bars | 2.6407 |
| exposure | 0.1958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
