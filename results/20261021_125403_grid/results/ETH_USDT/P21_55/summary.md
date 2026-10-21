# EMA Hourly Continuation — ETH/USDT P21_55

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6738 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.5937 |
| sortino_ratio | -0.7691 |
| max_drawdown | 0.6015 |
| cagr | -0.2955 |
| net_avg_win | 56.4616 |
| net_avg_loss | -84.9894 |
| avg_hold_time_bars | 9.1506 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
