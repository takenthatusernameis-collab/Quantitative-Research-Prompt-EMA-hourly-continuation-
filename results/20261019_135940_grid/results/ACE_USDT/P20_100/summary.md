# EMA Hourly Continuation — ACE/USDT P20_100

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.6978 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.4207 |
| sortino_ratio | -0.8014 |
| max_drawdown | 0.6214 |
| cagr | -0.3089 |
| net_avg_win | 52.2365 |
| net_avg_loss | -72.9527 |
| avg_hold_time_bars | 17.6519 |
| exposure | 0.4337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
