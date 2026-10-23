# EMA Hourly Continuation — KAVA/USDT P89_144

**Symbol:** KAVA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.3967 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.8303 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -6.6245 |
| sortino_ratio | -2.1538 |
| max_drawdown | 0.9359 |
| cagr | -0.6622 |
| net_avg_win | 28.0619 |
| net_avg_loss | -50.2940 |
| avg_hold_time_bars | 5.6395 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
