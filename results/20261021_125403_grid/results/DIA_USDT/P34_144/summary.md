# EMA Hourly Continuation — DIA/USDT P34_144

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.8211 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0336 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.2179 |
| sortino_ratio | -0.3544 |
| max_drawdown | 0.4189 |
| cagr | -0.1519 |
| net_avg_win | 73.9588 |
| net_avg_loss | -94.0874 |
| avg_hold_time_bars | 20.3923 |
| exposure | 0.3811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
