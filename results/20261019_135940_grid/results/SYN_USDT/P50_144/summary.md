# EMA Hourly Continuation — SYN/USDT P50_144

**Symbol:** SYN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6568 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.8657 |
| sortino_ratio | -0.8929 |
| max_drawdown | 0.6700 |
| cagr | -0.3413 |
| net_avg_win | 54.2818 |
| net_avg_loss | -74.8025 |
| avg_hold_time_bars | 13.8880 |
| exposure | 0.3043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
