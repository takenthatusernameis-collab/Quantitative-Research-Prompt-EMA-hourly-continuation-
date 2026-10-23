# EMA Hourly Continuation — DIA/USDT P50_100

**Symbol:** DIA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.9742 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -4.6268 |
| sortino_ratio | -1.6635 |
| max_drawdown | 0.8727 |
| cagr | -0.5507 |
| net_avg_win | 40.1969 |
| net_avg_loss | -61.1357 |
| avg_hold_time_bars | 6.1009 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
