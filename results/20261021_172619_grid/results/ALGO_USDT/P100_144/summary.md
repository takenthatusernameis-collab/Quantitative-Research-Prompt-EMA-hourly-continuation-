# EMA Hourly Continuation — ALGO/USDT P100_144

**Symbol:** ALGO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.7984 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0875 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -1.0017 |
| sortino_ratio | -0.2177 |
| max_drawdown | 0.2736 |
| cagr | -0.0957 |
| net_avg_win | 74.3241 |
| net_avg_loss | -102.5702 |
| avg_hold_time_bars | 5.8370 |
| exposure | 0.0602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
