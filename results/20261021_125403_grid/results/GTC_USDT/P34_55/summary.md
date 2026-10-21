# EMA Hourly Continuation — GTC/USDT P34_55

**Symbol:** GTC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9893 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.3294 |
| sortino_ratio | -0.6703 |
| max_drawdown | 0.5447 |
| cagr | -0.2639 |
| net_avg_win | 62.5580 |
| net_avg_loss | -87.7639 |
| avg_hold_time_bars | 5.8607 |
| exposure | 0.1071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
