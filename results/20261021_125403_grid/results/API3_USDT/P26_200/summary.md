# EMA Hourly Continuation — API3/USDT P26_200

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9723 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.1455 |
| sortino_ratio | -0.2884 |
| max_drawdown | 0.3797 |
| cagr | -0.1256 |
| net_avg_win | 83.7852 |
| net_avg_loss | -99.2374 |
| avg_hold_time_bars | 39.8939 |
| exposure | 0.5640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
