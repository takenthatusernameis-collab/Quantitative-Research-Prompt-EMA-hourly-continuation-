# EMA Hourly Continuation — KAVA/USDT P8_55

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.5755 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.9923 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -7.7993 |
| sortino_ratio | -3.6428 |
| max_drawdown | 0.9899 |
| cagr | -0.8373 |
| net_avg_win | 27.3213 |
| net_avg_loss | -37.4760 |
| avg_hold_time_bars | 10.0979 |
| exposure | 0.5109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
