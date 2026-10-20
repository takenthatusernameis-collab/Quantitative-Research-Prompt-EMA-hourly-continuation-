# EMA Hourly Continuation — ANKR/USDT P55_200

**Symbol:** ANKR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6291 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -3.1727 |
| sortino_ratio | -0.8930 |
| max_drawdown | 0.6713 |
| cagr | -0.3532 |
| net_avg_win | 59.0769 |
| net_avg_loss | -84.2039 |
| avg_hold_time_bars | 21.1040 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
