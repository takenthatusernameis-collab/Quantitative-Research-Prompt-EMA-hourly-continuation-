# EMA Hourly Continuation — BTC/USDT P8_144

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7149 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0105 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.7725 |
| sortino_ratio | -0.4584 |
| max_drawdown | 0.4689 |
| cagr | -0.1900 |
| net_avg_win | 60.6197 |
| net_avg_loss | -86.1727 |
| avg_hold_time_bars | 51.1995 |
| exposure | 0.7598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
