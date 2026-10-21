# EMA Hourly Continuation — DGB/USDT P89_200

**Symbol:** DGB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7343 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9294 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -1.7638 |
| sortino_ratio | -0.4380 |
| max_drawdown | 0.4166 |
| cagr | -0.1828 |
| net_avg_win | 75.7844 |
| net_avg_loss | -94.7142 |
| avg_hold_time_bars | 14.7426 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
