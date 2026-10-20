# EMA Hourly Continuation — MANTA/USDT P8_55

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.6348 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -5.3371 |
| sortino_ratio | -2.3043 |
| max_drawdown | 0.9385 |
| cagr | -0.6694 |
| net_avg_win | 37.4723 |
| net_avg_loss | -50.5506 |
| avg_hold_time_bars | 13.0042 |
| exposure | 0.5574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
