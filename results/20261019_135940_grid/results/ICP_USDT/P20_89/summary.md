# EMA Hourly Continuation — ICP/USDT P20_89

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.6013 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -4.6432 |
| sortino_ratio | -1.7749 |
| max_drawdown | 0.8949 |
| cagr | -0.5821 |
| net_avg_win | 37.1080 |
| net_avg_loss | -56.9777 |
| avg_hold_time_bars | 11.2447 |
| exposure | 0.3844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
