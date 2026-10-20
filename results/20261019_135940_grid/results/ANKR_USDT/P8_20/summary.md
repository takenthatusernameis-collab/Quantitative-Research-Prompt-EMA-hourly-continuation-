# EMA Hourly Continuation — ANKR/USDT P8_20

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1652 |
| net_profit_factor | 0.3312 |
| net_win_rate | 0.4086 |
| gross_profit_factor | 0.7755 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -13.6875 |
| sortino_ratio | -7.8922 |
| max_drawdown | 1.0000 |
| cagr | -0.9825 |
| net_avg_win | 7.3366 |
| net_avg_loss | -15.3038 |
| avg_hold_time_bars | 3.2361 |
| exposure | 0.2430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
