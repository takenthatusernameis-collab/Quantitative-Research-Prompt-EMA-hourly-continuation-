# EMA Hourly Continuation — JST/USDT P26_100

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6311 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0715 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -2.7778 |
| sortino_ratio | -0.8189 |
| max_drawdown | 0.6413 |
| cagr | -0.3205 |
| net_avg_win | 47.5455 |
| net_avg_loss | -80.3660 |
| avg_hold_time_bars | 16.4240 |
| exposure | 0.3225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
