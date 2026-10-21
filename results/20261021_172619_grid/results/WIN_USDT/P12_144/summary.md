# EMA Hourly Continuation — WIN/USDT P12_144

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8115 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0352 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -1.0328 |
| sortino_ratio | -0.2791 |
| max_drawdown | 0.4034 |
| cagr | -0.1226 |
| net_avg_win | 65.8607 |
| net_avg_loss | -86.8524 |
| avg_hold_time_bars | 41.6667 |
| exposure | 0.6705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
