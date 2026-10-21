# EMA Hourly Continuation — ETH/USDT P50_89

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0226 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.0946 |
| sortino_ratio | -0.4952 |
| max_drawdown | 0.4537 |
| cagr | -0.2020 |
| net_avg_win | 62.6385 |
| net_avg_loss | -96.5803 |
| avg_hold_time_bars | 7.9480 |
| exposure | 0.0972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
