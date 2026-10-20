# EMA Hourly Continuation — FLIP/USDT P8_26

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.3496 |
| net_win_rate | 0.3769 |
| gross_profit_factor | 0.7520 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -11.0386 |
| sortino_ratio | -5.0803 |
| max_drawdown | 0.9986 |
| cagr | -0.9261 |
| net_avg_win | 13.4847 |
| net_avg_loss | -23.3321 |
| avg_hold_time_bars | 7.3097 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
