# EMA Hourly Continuation — BTC/USDT P12_89

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.6525 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -2.6118 |
| sortino_ratio | -0.7916 |
| max_drawdown | 0.6491 |
| cagr | -0.3031 |
| net_avg_win | 47.3564 |
| net_avg_loss | -73.7355 |
| avg_hold_time_bars | 26.7154 |
| exposure | 0.5407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
