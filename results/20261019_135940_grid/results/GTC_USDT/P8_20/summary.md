# EMA Hourly Continuation — GTC/USDT P8_20

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1423 |
| net_profit_factor | 0.3861 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.8408 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -10.3142 |
| sortino_ratio | -5.5034 |
| max_drawdown | 0.9989 |
| cagr | -0.9336 |
| net_avg_win | 10.3490 |
| net_avg_loss | -19.9397 |
| avg_hold_time_bars | 3.7337 |
| exposure | 0.2415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
