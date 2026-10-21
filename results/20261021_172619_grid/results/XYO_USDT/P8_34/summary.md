# EMA Hourly Continuation — XYO/USDT P8_34

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.6027 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8299 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -4.7489 |
| sortino_ratio | -1.8532 |
| max_drawdown | 0.8844 |
| cagr | -0.5738 |
| net_avg_win | 39.6576 |
| net_avg_loss | -53.2090 |
| avg_hold_time_bars | 8.4114 |
| exposure | 0.2878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
