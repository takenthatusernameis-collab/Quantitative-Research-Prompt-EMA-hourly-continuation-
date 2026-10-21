# EMA Hourly Continuation — ZRX/USDT P34_200

**Symbol:** ZRX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7689 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.4735 |
| sortino_ratio | -0.3812 |
| max_drawdown | 0.3955 |
| cagr | -0.1620 |
| net_avg_win | 73.5994 |
| net_avg_loss | -92.8537 |
| avg_hold_time_bars | 33.8571 |
| exposure | 0.5063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
