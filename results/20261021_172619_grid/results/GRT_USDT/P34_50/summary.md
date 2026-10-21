# EMA Hourly Continuation — GRT/USDT P34_50

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.7466 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0686 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -1.3339 |
| sortino_ratio | -0.3020 |
| max_drawdown | 0.3491 |
| cagr | -0.1284 |
| net_avg_win | 66.9252 |
| net_avg_loss | -97.9980 |
| avg_hold_time_bars | 4.9150 |
| exposure | 0.0549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
