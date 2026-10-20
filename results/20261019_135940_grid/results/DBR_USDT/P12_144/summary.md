# EMA Hourly Continuation — DBR/USDT P12_144

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.4686 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.7195 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -4.6112 |
| sortino_ratio | -1.4346 |
| max_drawdown | 0.7561 |
| cagr | -0.5005 |
| net_avg_win | 38.7582 |
| net_avg_loss | -63.1463 |
| avg_hold_time_bars | 28.1367 |
| exposure | 0.6320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
