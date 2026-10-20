# EMA Hourly Continuation — FLIP/USDT P20_26

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.1962 |
| net_win_rate | 0.3226 |
| gross_profit_factor | 0.7200 |
| gross_win_rate | 0.4076 |
| sharpe_ratio | -13.5398 |
| sortino_ratio | -5.9303 |
| max_drawdown | 0.9997 |
| cagr | -0.9602 |
| net_avg_win | 8.6820 |
| net_avg_loss | -21.0790 |
| avg_hold_time_bars | 4.1309 |
| exposure | 0.1635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
