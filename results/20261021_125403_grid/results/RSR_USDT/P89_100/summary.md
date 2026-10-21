# EMA Hourly Continuation — RSR/USDT P89_100

**Symbol:** RSR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 126 |
| net_profit_factor | 0.9000 |
| net_win_rate | 0.5476 |
| gross_profit_factor | 1.2101 |
| gross_win_rate | 0.5476 |
| sharpe_ratio | -0.3655 |
| sortino_ratio | -0.0596 |
| max_drawdown | 0.2178 |
| cagr | -0.0280 |
| net_avg_win | 89.7452 |
| net_avg_loss | -120.7118 |
| avg_hold_time_bars | 4.3175 |
| exposure | 0.0247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
