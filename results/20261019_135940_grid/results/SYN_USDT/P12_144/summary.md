# EMA Hourly Continuation — SYN/USDT P12_144

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7592 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9975 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.8791 |
| sortino_ratio | -0.5732 |
| max_drawdown | 0.5197 |
| cagr | -0.2387 |
| net_avg_win | 67.6695 |
| net_avg_loss | -87.9946 |
| avg_hold_time_bars | 33.2882 |
| exposure | 0.7036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
