# EMA Hourly Continuation — RAY/USDT P100_144

**Symbol:** RAY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.6753 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -1.6552 |
| sortino_ratio | -0.3498 |
| max_drawdown | 0.3738 |
| cagr | -0.1480 |
| net_avg_win | 65.6189 |
| net_avg_loss | -89.4961 |
| avg_hold_time_bars | 7.6301 |
| exposure | 0.0760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
