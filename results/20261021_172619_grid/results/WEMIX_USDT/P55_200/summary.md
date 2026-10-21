# EMA Hourly Continuation — WEMIX/USDT P55_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.4857 |
| net_win_rate | 0.3746 |
| gross_profit_factor | 0.6054 |
| gross_win_rate | 0.3746 |
| sharpe_ratio | -4.3507 |
| sortino_ratio | -1.1532 |
| max_drawdown | 0.7416 |
| cagr | -0.4147 |
| net_avg_win | 52.5068 |
| net_avg_loss | -64.7684 |
| avg_hold_time_bars | 22.5183 |
| exposure | 0.3634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
