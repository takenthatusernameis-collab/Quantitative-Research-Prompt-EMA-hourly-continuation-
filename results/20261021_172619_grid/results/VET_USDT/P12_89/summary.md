# EMA Hourly Continuation — VET/USDT P12_89

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.8126 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0319 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.3514 |
| sortino_ratio | -0.4373 |
| max_drawdown | 0.4412 |
| cagr | -0.1839 |
| net_avg_win | 66.3738 |
| net_avg_loss | -86.3148 |
| avg_hold_time_bars | 22.6122 |
| exposure | 0.5221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
