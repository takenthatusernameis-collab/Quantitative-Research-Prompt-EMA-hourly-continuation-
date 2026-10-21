# EMA Hourly Continuation — ETH/USDT P55_89

**Symbol:** ETH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7021 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1160 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -1.6462 |
| sortino_ratio | -0.3731 |
| max_drawdown | 0.3685 |
| cagr | -0.1556 |
| net_avg_win | 62.7409 |
| net_avg_loss | -101.0144 |
| avg_hold_time_bars | 7.4939 |
| exposure | 0.0835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
