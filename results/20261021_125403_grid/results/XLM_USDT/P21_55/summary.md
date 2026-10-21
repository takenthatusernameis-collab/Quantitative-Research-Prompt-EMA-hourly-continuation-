# EMA Hourly Continuation — XLM/USDT P21_55

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6501 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9640 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -2.6105 |
| sortino_ratio | -0.8299 |
| max_drawdown | 0.6256 |
| cagr | -0.3151 |
| net_avg_win | 46.7172 |
| net_avg_loss | -71.2736 |
| avg_hold_time_bars | 8.7122 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
