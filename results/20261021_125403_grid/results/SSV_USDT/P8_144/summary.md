# EMA Hourly Continuation — SSV/USDT P8_144

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.8363 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9723 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -0.9639 |
| sortino_ratio | -0.2449 |
| max_drawdown | 0.3111 |
| cagr | -0.1084 |
| net_avg_win | 81.8292 |
| net_avg_loss | -95.4110 |
| avg_hold_time_bars | 54.5912 |
| exposure | 0.7856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
