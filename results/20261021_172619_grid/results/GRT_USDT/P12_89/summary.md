# EMA Hourly Continuation — GRT/USDT P12_89

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.8029 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.7395 |
| sortino_ratio | -0.5518 |
| max_drawdown | 0.5534 |
| cagr | -0.2256 |
| net_avg_win | 79.3528 |
| net_avg_loss | -95.6963 |
| avg_hold_time_bars | 22.9637 |
| exposure | 0.5154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
