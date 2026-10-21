# EMA Hourly Continuation — LINK/USDT P100_144

**Symbol:** LINK/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.4074 |
| sortino_ratio | -0.2792 |
| max_drawdown | 0.3024 |
| cagr | -0.1190 |
| net_avg_win | 66.4159 |
| net_avg_loss | -96.8253 |
| avg_hold_time_bars | 6.5789 |
| exposure | 0.0568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
