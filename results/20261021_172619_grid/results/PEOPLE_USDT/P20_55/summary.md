# EMA Hourly Continuation — PEOPLE/USDT P20_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.7591 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.2333 |
| sortino_ratio | -0.7575 |
| max_drawdown | 0.5936 |
| cagr | -0.2937 |
| net_avg_win | 66.4211 |
| net_avg_loss | -84.1628 |
| avg_hold_time_bars | 8.0956 |
| exposure | 0.2070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
