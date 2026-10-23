# EMA Hourly Continuation — NMR/USDT P26_50

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1025 |
| net_profit_factor | 0.5238 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.9476 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -8.3102 |
| sortino_ratio | -3.7393 |
| max_drawdown | 0.9911 |
| cagr | -0.8453 |
| net_avg_win | 24.1117 |
| net_avg_loss | -36.3112 |
| avg_hold_time_bars | 3.9639 |
| exposure | 0.1847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
