# EMA Hourly Continuation — ZEC/USDT P100_144

**Symbol:** ZEC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.7776 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 0.9972 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.0513 |
| sortino_ratio | -0.2250 |
| max_drawdown | 0.2579 |
| cagr | -0.0985 |
| net_avg_win | 70.9760 |
| net_avg_loss | -93.7609 |
| avg_hold_time_bars | 6.5471 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
