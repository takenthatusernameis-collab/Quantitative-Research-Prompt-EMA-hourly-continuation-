# EMA Hourly Continuation — XRP/USDT P26_55

**Symbol:** XRP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6208 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -2.8335 |
| sortino_ratio | -0.7953 |
| max_drawdown | 0.6151 |
| cagr | -0.3028 |
| net_avg_win | 52.4449 |
| net_avg_loss | -80.5752 |
| avg_hold_time_bars | 6.9134 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
