# EMA Hourly Continuation — ENJ/USDT P20_50

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.7483 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0241 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.1729 |
| sortino_ratio | -0.7172 |
| max_drawdown | 0.5933 |
| cagr | -0.2802 |
| net_avg_win | 62.5218 |
| net_avg_loss | -84.8205 |
| avg_hold_time_bars | 6.8402 |
| exposure | 0.1647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
