# EMA Hourly Continuation — APE/USDT P20_21

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 124 |
| net_profit_factor | 0.5856 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8186 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -1.8406 |
| sortino_ratio | -0.2926 |
| max_drawdown | 0.2980 |
| cagr | -0.1263 |
| net_avg_win | 72.5590 |
| net_avg_loss | -102.0373 |
| avg_hold_time_bars | 3.5806 |
| exposure | 0.0202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
