# EMA Hourly Continuation — FIL/USDT P89_100

**Symbol:** FIL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 81 |
| net_profit_factor | 0.9604 |
| net_win_rate | 0.5802 |
| gross_profit_factor | 1.3681 |
| gross_win_rate | 0.5802 |
| sharpe_ratio | -0.0818 |
| sortino_ratio | -0.0108 |
| max_drawdown | 0.0763 |
| cagr | -0.0062 |
| net_avg_win | 80.4327 |
| net_avg_loss | -115.7742 |
| avg_hold_time_bars | 5.2963 |
| exposure | 0.0195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
