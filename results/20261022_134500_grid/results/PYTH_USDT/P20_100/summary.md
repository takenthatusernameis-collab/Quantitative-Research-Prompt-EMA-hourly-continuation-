# EMA Hourly Continuation — PYTH/USDT P20_100

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.6031 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8844 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -3.9989 |
| sortino_ratio | -1.4461 |
| max_drawdown | 0.8286 |
| cagr | -0.4979 |
| net_avg_win | 40.5826 |
| net_avg_loss | -58.7156 |
| avg_hold_time_bars | 14.3752 |
| exposure | 0.4319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
