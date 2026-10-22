# EMA Hourly Continuation — SNX/USDT P12_34

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1261 |
| net_profit_factor | 0.5299 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -7.7196 |
| sortino_ratio | -3.8564 |
| max_drawdown | 0.9912 |
| cagr | -0.8456 |
| net_avg_win | 19.1909 |
| net_avg_loss | -31.0447 |
| avg_hold_time_bars | 4.3069 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
