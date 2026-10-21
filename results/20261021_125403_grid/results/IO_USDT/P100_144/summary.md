# EMA Hourly Continuation — IO/USDT P100_144

**Symbol:** IO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9864 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0873 |
| sortino_ratio | -0.2407 |
| max_drawdown | 0.2424 |
| cagr | -0.1054 |
| net_avg_win | 77.2826 |
| net_avg_loss | -97.9056 |
| avg_hold_time_bars | 6.7946 |
| exposure | 0.0737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
