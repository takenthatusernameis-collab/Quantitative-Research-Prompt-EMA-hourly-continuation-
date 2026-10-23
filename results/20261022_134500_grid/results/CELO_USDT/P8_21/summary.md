# EMA Hourly Continuation — CELO/USDT P8_21

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1644 |
| net_profit_factor | 0.3386 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.7269 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -11.8157 |
| sortino_ratio | -6.7430 |
| max_drawdown | 0.9998 |
| cagr | -0.9664 |
| net_avg_win | 7.3538 |
| net_avg_loss | -15.9455 |
| avg_hold_time_bars | 3.2238 |
| exposure | 0.2398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
