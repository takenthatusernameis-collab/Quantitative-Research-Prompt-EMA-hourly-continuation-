# EMA Hourly Continuation — BNB/USDT P89_100

**Symbol:** BNB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 94 |
| net_profit_factor | 0.5616 |
| net_win_rate | 0.5319 |
| gross_profit_factor | 1.1955 |
| gross_win_rate | 0.5426 |
| sharpe_ratio | -1.6325 |
| sortino_ratio | -0.2318 |
| max_drawdown | 0.2409 |
| cagr | -0.0976 |
| net_avg_win | 58.2209 |
| net_avg_loss | -117.8168 |
| avg_hold_time_bars | 4.0213 |
| exposure | 0.0172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
