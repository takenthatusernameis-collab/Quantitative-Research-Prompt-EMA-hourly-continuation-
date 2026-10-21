# EMA Hourly Continuation — STRK/USDT P50_144

**Symbol:** STRK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8974 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.0929 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -0.5669 |
| sortino_ratio | -0.1538 |
| max_drawdown | 0.3078 |
| cagr | -0.0716 |
| net_avg_win | 80.0768 |
| net_avg_loss | -98.7894 |
| avg_hold_time_bars | 15.7373 |
| exposure | 0.2532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
