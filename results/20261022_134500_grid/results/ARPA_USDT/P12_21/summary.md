# EMA Hourly Continuation — ARPA/USDT P12_21

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1507 |
| net_profit_factor | 0.3370 |
| net_win_rate | 0.3928 |
| gross_profit_factor | 0.8959 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -13.7302 |
| sortino_ratio | -7.6132 |
| max_drawdown | 0.9999 |
| cagr | -0.9796 |
| net_avg_win | 8.5858 |
| net_avg_loss | -16.4833 |
| avg_hold_time_bars | 2.9668 |
| exposure | 0.2023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
