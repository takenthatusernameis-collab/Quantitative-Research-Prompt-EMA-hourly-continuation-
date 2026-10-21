# EMA Hourly Continuation — LSK/USDT P50_144

**Symbol:** LSK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 0.9981 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.5986 |
| sortino_ratio | -0.4442 |
| max_drawdown | 0.4943 |
| cagr | -0.1856 |
| net_avg_win | 63.9152 |
| net_avg_loss | -86.9477 |
| avg_hold_time_bars | 17.7154 |
| exposure | 0.3028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
