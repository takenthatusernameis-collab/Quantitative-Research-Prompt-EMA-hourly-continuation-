# EMA Hourly Continuation — XAI/USDT P26_144

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7269 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9753 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -2.8941 |
| sortino_ratio | -0.8968 |
| max_drawdown | 0.7225 |
| cagr | -0.3509 |
| net_avg_win | 75.6371 |
| net_avg_loss | -93.9769 |
| avg_hold_time_bars | 23.2383 |
| exposure | 0.5186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
