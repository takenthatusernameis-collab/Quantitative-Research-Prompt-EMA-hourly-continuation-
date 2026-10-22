# EMA Hourly Continuation — SATS/USDT P100_144

**Symbol:** SATS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.6005 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8070 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -2.4416 |
| sortino_ratio | -0.5356 |
| max_drawdown | 0.4688 |
| cagr | -0.2190 |
| net_avg_win | 65.7985 |
| net_avg_loss | -87.3298 |
| avg_hold_time_bars | 7.9205 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
