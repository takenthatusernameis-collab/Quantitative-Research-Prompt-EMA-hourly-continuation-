# EMA Hourly Continuation — ZIL/USDT P26_55

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.4269 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8221 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -7.7474 |
| sortino_ratio | -3.3813 |
| max_drawdown | 0.9842 |
| cagr | -0.8063 |
| net_avg_win | 17.4073 |
| net_avg_loss | -33.0758 |
| avg_hold_time_bars | 4.1085 |
| exposure | 0.1755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
