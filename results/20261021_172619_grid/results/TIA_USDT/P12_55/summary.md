# EMA Hourly Continuation — TIA/USDT P12_55

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.8808 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0619 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -0.9501 |
| sortino_ratio | -0.3294 |
| max_drawdown | 0.4333 |
| cagr | -0.1447 |
| net_avg_win | 79.7224 |
| net_avg_loss | -96.9505 |
| avg_hold_time_bars | 13.1546 |
| exposure | 0.3480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
