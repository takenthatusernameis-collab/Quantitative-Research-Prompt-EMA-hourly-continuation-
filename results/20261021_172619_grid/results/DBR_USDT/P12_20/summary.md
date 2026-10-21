# EMA Hourly Continuation — DBR/USDT P12_20

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.5640 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 1.0365 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.7625 |
| sortino_ratio | -1.0864 |
| max_drawdown | 0.6749 |
| cagr | -0.3961 |
| net_avg_win | 52.4610 |
| net_avg_loss | -86.4103 |
| avg_hold_time_bars | 6.5828 |
| exposure | 0.1220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
