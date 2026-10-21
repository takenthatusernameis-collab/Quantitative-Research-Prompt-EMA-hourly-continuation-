# EMA Hourly Continuation — DCR/USDT P12_50

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6979 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.7858 |
| sortino_ratio | -1.0587 |
| max_drawdown | 0.7269 |
| cagr | -0.3865 |
| net_avg_win | 47.0201 |
| net_avg_loss | -64.7726 |
| avg_hold_time_bars | 9.6972 |
| exposure | 0.3116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
