# EMA Hourly Continuation — DOT/USDT P12_200

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.8592 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -0.6429 |
| sortino_ratio | -0.1306 |
| max_drawdown | 0.1994 |
| cagr | -0.0600 |
| net_avg_win | 86.1053 |
| net_avg_loss | -103.2545 |
| avg_hold_time_bars | 88.0299 |
| exposure | 0.8043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
