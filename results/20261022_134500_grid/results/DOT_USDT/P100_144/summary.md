# EMA Hourly Continuation — DOT/USDT P100_144

**Symbol:** DOT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.4231 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8795 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -5.7947 |
| sortino_ratio | -1.7327 |
| max_drawdown | 0.8909 |
| cagr | -0.5824 |
| net_avg_win | 33.7664 |
| net_avg_loss | -60.8747 |
| avg_hold_time_bars | 3.3812 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
