# EMA Hourly Continuation — ACE/USDT P55_100

**Symbol:** ACE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0571 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -2.9945 |
| sortino_ratio | -0.9512 |
| max_drawdown | 0.6802 |
| cagr | -0.3605 |
| net_avg_win | 47.3897 |
| net_avg_loss | -74.3313 |
| avg_hold_time_bars | 7.0319 |
| exposure | 0.1597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
