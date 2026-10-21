# EMA Hourly Continuation — W/USDT P12_50

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.8121 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.6902 |
| sortino_ratio | -0.6102 |
| max_drawdown | 0.5425 |
| cagr | -0.2464 |
| net_avg_win | 69.3561 |
| net_avg_loss | -84.8648 |
| avg_hold_time_bars | 11.0110 |
| exposure | 0.3183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
