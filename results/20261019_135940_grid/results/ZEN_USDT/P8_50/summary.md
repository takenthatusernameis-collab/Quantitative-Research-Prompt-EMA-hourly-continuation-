# EMA Hourly Continuation — ZEN/USDT P8_50

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1194 |
| net_profit_factor | 0.4883 |
| net_win_rate | 0.4363 |
| gross_profit_factor | 0.8224 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -7.6275 |
| sortino_ratio | -3.6899 |
| max_drawdown | 0.9896 |
| cagr | -0.8365 |
| net_avg_win | 18.1241 |
| net_avg_loss | -28.7320 |
| avg_hold_time_bars | 8.5151 |
| exposure | 0.4621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
