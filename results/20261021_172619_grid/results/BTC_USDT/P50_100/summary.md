# EMA Hourly Continuation — BTC/USDT P50_100

**Symbol:** BTC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.5868 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0451 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -2.8758 |
| sortino_ratio | -0.7253 |
| max_drawdown | 0.6166 |
| cagr | -0.2817 |
| net_avg_win | 49.0268 |
| net_avg_loss | -87.4983 |
| avg_hold_time_bars | 10.2139 |
| exposure | 0.1414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
