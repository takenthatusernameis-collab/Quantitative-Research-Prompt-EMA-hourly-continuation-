# EMA Hourly Continuation — REQ/USDT P12_144

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.8343 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -3.8302 |
| sortino_ratio | -1.2084 |
| max_drawdown | 0.7619 |
| cagr | -0.4284 |
| net_avg_win | 56.8247 |
| net_avg_loss | -72.2211 |
| avg_hold_time_bars | 25.8644 |
| exposure | 0.5808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
