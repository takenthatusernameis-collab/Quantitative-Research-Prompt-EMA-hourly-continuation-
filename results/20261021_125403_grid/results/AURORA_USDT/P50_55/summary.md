# EMA Hourly Continuation — AURORA/USDT P50_55

**Symbol:** AURORA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.4444 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.7779 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -2.9704 |
| sortino_ratio | -0.5051 |
| max_drawdown | 0.4709 |
| cagr | -0.2129 |
| net_avg_win | 59.2475 |
| net_avg_loss | -102.9489 |
| avg_hold_time_bars | 7.2143 |
| exposure | 0.0459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
