# EMA Hourly Continuation — WEMIX/USDT P100_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 790 |
| net_profit_factor | 0.2056 |
| net_win_rate | 0.2658 |
| gross_profit_factor | 0.4001 |
| gross_win_rate | 0.2810 |
| sharpe_ratio | -13.3335 |
| sortino_ratio | -5.4640 |
| max_drawdown | 0.9993 |
| cagr | -0.9430 |
| net_avg_win | 12.3143 |
| net_avg_loss | -21.6871 |
| avg_hold_time_bars | 3.5911 |
| exposure | 0.1290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
