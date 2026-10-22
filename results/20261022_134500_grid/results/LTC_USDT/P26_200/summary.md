# EMA Hourly Continuation — LTC/USDT P26_200

**Symbol:** LTC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.4374 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7727 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -4.2541 |
| sortino_ratio | -1.1776 |
| max_drawdown | 0.7660 |
| cagr | -0.4298 |
| net_avg_win | 35.1969 |
| net_avg_loss | -61.3631 |
| avg_hold_time_bars | 33.4145 |
| exposure | 0.5863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
