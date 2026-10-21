# EMA Hourly Continuation — ONT/USDT P100_144

**Symbol:** ONT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.5484 |
| sortino_ratio | -0.3474 |
| max_drawdown | 0.3725 |
| cagr | -0.1476 |
| net_avg_win | 67.2268 |
| net_avg_loss | -97.6637 |
| avg_hold_time_bars | 6.2245 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
