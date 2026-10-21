# EMA Hourly Continuation — LPT/USDT P100_144

**Symbol:** LPT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6071 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8300 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -2.5279 |
| sortino_ratio | -0.5915 |
| max_drawdown | 0.5040 |
| cagr | -0.2374 |
| net_avg_win | 62.0347 |
| net_avg_loss | -86.0809 |
| avg_hold_time_bars | 6.4870 |
| exposure | 0.0793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
