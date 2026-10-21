# EMA Hourly Continuation — HTX/USDT P100_144

**Symbol:** HTX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.2916 |
| net_win_rate | 0.3178 |
| gross_profit_factor | 0.5595 |
| gross_win_rate | 0.3217 |
| sharpe_ratio | -6.5284 |
| sortino_ratio | -1.5442 |
| max_drawdown | 0.8474 |
| cagr | -0.5211 |
| net_avg_win | 42.3685 |
| net_avg_loss | -67.6883 |
| avg_hold_time_bars | 7.0853 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
