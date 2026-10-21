# EMA Hourly Continuation — ILV/USDT P34_144

**Symbol:** ILV/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.9187 |
| net_win_rate | 0.5349 |
| gross_profit_factor | 1.1391 |
| gross_win_rate | 0.5349 |
| sharpe_ratio | -0.4546 |
| sortino_ratio | -0.1293 |
| max_drawdown | 0.1867 |
| cagr | -0.0619 |
| net_avg_win | 80.9580 |
| net_avg_loss | -101.3430 |
| avg_hold_time_bars | 23.3127 |
| exposure | 0.4101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
