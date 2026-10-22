# EMA Hourly Continuation — CAKE/USDT P8_20

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1639 |
| net_profit_factor | 0.3227 |
| net_win_rate | 0.4039 |
| gross_profit_factor | 0.8888 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -14.2172 |
| sortino_ratio | -8.1987 |
| max_drawdown | 1.0000 |
| cagr | -0.9862 |
| net_avg_win | 7.1980 |
| net_avg_loss | -15.1124 |
| avg_hold_time_bars | 2.9725 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
