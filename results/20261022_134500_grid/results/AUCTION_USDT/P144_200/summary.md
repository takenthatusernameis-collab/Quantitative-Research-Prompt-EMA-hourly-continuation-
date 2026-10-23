# EMA Hourly Continuation — AUCTION/USDT P144_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.4251 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.8204 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -6.1961 |
| sortino_ratio | -1.8124 |
| max_drawdown | 0.9084 |
| cagr | -0.6118 |
| net_avg_win | 36.4961 |
| net_avg_loss | -61.7022 |
| avg_hold_time_bars | 6.1682 |
| exposure | 0.1228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
