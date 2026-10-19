# EMA Hourly Continuation — SUN/USDT P12_89

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.4299 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.9135 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -7.4620 |
| sortino_ratio | -2.6869 |
| max_drawdown | 0.9703 |
| cagr | -0.7461 |
| net_avg_win | 25.9934 |
| net_avg_loss | -44.9451 |
| avg_hold_time_bars | 17.9272 |
| exposure | 0.5346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
