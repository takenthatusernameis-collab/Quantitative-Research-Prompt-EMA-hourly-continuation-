# EMA Hourly Continuation — MOVR/USDT P12_144

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.5972 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -3.6599 |
| sortino_ratio | -1.2172 |
| max_drawdown | 0.7833 |
| cagr | -0.4403 |
| net_avg_win | 44.4244 |
| net_avg_loss | -62.8531 |
| avg_hold_time_bars | 26.1789 |
| exposure | 0.6652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
