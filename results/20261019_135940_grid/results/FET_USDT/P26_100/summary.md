# EMA Hourly Continuation — FET/USDT P26_100

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6974 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9919 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -2.7109 |
| sortino_ratio | -0.9532 |
| max_drawdown | 0.6983 |
| cagr | -0.3618 |
| net_avg_win | 51.1058 |
| net_avg_loss | -72.0960 |
| avg_hold_time_bars | 12.2911 |
| exposure | 0.3436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
