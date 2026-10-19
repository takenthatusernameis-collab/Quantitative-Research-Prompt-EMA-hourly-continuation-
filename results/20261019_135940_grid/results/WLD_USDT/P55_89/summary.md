# EMA Hourly Continuation — WLD/USDT P55_89

**Symbol:** WLD/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.6182 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 1.0040 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -3.7251 |
| sortino_ratio | -1.3015 |
| max_drawdown | 0.7912 |
| cagr | -0.4610 |
| net_avg_win | 42.9636 |
| net_avg_loss | -66.5865 |
| avg_hold_time_bars | 4.2389 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
