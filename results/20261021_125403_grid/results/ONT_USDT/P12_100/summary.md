# EMA Hourly Continuation — ONT/USDT P12_100

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9079 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.1969 |
| sortino_ratio | -0.7099 |
| max_drawdown | 0.5865 |
| cagr | -0.2796 |
| net_avg_win | 64.7455 |
| net_avg_loss | -79.2489 |
| avg_hold_time_bars | 23.0058 |
| exposure | 0.5393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
