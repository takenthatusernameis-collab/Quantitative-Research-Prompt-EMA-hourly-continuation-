# EMA Hourly Continuation — AXS/USDT P55_144

**Symbol:** AXS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.9278 |
| net_win_rate | 0.5480 |
| gross_profit_factor | 1.2006 |
| gross_win_rate | 0.5480 |
| sharpe_ratio | -0.3736 |
| sortino_ratio | -0.0972 |
| max_drawdown | 0.1885 |
| cagr | -0.0474 |
| net_avg_win | 83.7350 |
| net_avg_loss | -109.4111 |
| avg_hold_time_bars | 15.6502 |
| exposure | 0.2287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
