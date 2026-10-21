# EMA Hourly Continuation — ETHFI/USDT P12_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8380 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9700 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -1.2701 |
| sortino_ratio | -0.3901 |
| max_drawdown | 0.4174 |
| cagr | -0.1667 |
| net_avg_win | 83.7442 |
| net_avg_loss | -96.1176 |
| avg_hold_time_bars | 26.6911 |
| exposure | 0.5617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
