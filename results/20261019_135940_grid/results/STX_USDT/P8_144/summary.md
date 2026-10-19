# EMA Hourly Continuation — STX/USDT P8_144

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6602 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.4602 |
| sortino_ratio | -0.6965 |
| max_drawdown | 0.6306 |
| cagr | -0.2857 |
| net_avg_win | 56.1284 |
| net_avg_loss | -78.2995 |
| avg_hold_time_bars | 42.1695 |
| exposure | 0.7881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
