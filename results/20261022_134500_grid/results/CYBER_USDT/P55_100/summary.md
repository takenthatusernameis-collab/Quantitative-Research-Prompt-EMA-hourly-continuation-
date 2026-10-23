# EMA Hourly Continuation — CYBER/USDT P55_100

**Symbol:** CYBER/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6023 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -3.5718 |
| sortino_ratio | -1.2671 |
| max_drawdown | 0.8007 |
| cagr | -0.4497 |
| net_avg_win | 37.3508 |
| net_avg_loss | -63.6295 |
| avg_hold_time_bars | 5.5981 |
| exposure | 0.1583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
