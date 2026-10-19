# EMA Hourly Continuation — ALGO/USDT P34_144

**Symbol:** ALGO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6587 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0073 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -2.7536 |
| sortino_ratio | -0.8671 |
| max_drawdown | 0.6531 |
| cagr | -0.3376 |
| net_avg_win | 49.5669 |
| net_avg_loss | -75.8531 |
| avg_hold_time_bars | 15.6400 |
| exposure | 0.3555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
