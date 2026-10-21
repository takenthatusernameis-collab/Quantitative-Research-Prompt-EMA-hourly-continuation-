# EMA Hourly Continuation — TAO/USDT P12_89

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.9277 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0930 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.5253 |
| sortino_ratio | -0.1668 |
| max_drawdown | 0.3164 |
| cagr | -0.0796 |
| net_avg_win | 94.9559 |
| net_avg_loss | -112.0649 |
| avg_hold_time_bars | 23.2695 |
| exposure | 0.5140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
