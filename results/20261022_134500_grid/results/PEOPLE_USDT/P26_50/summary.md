# EMA Hourly Continuation — PEOPLE/USDT P26_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.4697 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.7597 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -6.9841 |
| sortino_ratio | -2.9622 |
| max_drawdown | 0.9735 |
| cagr | -0.7622 |
| net_avg_win | 21.6089 |
| net_avg_loss | -35.9905 |
| avg_hold_time_bars | 4.0484 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
