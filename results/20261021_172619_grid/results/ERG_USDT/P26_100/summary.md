# EMA Hourly Continuation — ERG/USDT P26_100

**Symbol:** ERG/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.6054 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.7717 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -3.2325 |
| sortino_ratio | -0.9413 |
| max_drawdown | 0.6753 |
| cagr | -0.3519 |
| net_avg_win | 55.3234 |
| net_avg_loss | -70.6502 |
| avg_hold_time_bars | 13.4100 |
| exposure | 0.2572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
