# EMA Hourly Continuation — AR/USDT P12_21

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7442 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0096 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6741 |
| sortino_ratio | -0.4146 |
| max_drawdown | 0.4119 |
| cagr | -0.1732 |
| net_avg_win | 74.1553 |
| net_avg_loss | -99.6406 |
| avg_hold_time_bars | 5.1678 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
