# EMA Hourly Continuation — SKL/USDT P89_144

**Symbol:** SKL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8987 |
| net_win_rate | 0.5432 |
| gross_profit_factor | 1.1754 |
| gross_win_rate | 0.5432 |
| sharpe_ratio | -0.5026 |
| sortino_ratio | -0.1215 |
| max_drawdown | 0.2399 |
| cagr | -0.0567 |
| net_avg_win | 80.1661 |
| net_avg_loss | -106.0602 |
| avg_hold_time_bars | 8.4209 |
| exposure | 0.1064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
