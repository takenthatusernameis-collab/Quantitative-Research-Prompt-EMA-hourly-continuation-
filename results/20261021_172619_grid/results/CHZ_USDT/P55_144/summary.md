# EMA Hourly Continuation — CHZ/USDT P55_144

**Symbol:** CHZ/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7060 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9064 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -1.9535 |
| sortino_ratio | -0.5088 |
| max_drawdown | 0.4654 |
| cagr | -0.2093 |
| net_avg_win | 67.3013 |
| net_avg_loss | -86.6117 |
| avg_hold_time_bars | 15.5030 |
| exposure | 0.2354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
