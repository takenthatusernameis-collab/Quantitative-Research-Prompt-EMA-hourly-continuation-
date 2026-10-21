# EMA Hourly Continuation — DUSK/USDT P20_100

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7875 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.7620 |
| sortino_ratio | -0.5540 |
| max_drawdown | 0.5430 |
| cagr | -0.2264 |
| net_avg_win | 75.2450 |
| net_avg_loss | -88.3725 |
| avg_hold_time_bars | 17.7454 |
| exposure | 0.3928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
