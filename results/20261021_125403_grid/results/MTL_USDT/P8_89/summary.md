# EMA Hourly Continuation — MTL/USDT P8_89

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.7041 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9206 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.7899 |
| sortino_ratio | -0.8279 |
| max_drawdown | 0.6433 |
| cagr | -0.3202 |
| net_avg_win | 72.5731 |
| net_avg_loss | -89.4809 |
| avg_hold_time_bars | 36.4579 |
| exposure | 0.7243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
