# EMA Hourly Continuation — WLD/USDT P21_26

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 129 |
| net_profit_factor | 0.7965 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0453 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -0.8015 |
| sortino_ratio | -0.1309 |
| max_drawdown | 0.1926 |
| cagr | -0.0584 |
| net_avg_win | 83.2072 |
| net_avg_loss | -109.4381 |
| avg_hold_time_bars | 3.9302 |
| exposure | 0.0230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
