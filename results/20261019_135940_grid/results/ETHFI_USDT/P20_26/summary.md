# EMA Hourly Continuation — ETHFI/USDT P20_26

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1235 |
| net_profit_factor | 0.3616 |
| net_win_rate | 0.3757 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.3951 |
| sharpe_ratio | -13.2601 |
| sortino_ratio | -6.6901 |
| max_drawdown | 0.9998 |
| cagr | -0.9695 |
| net_avg_win | 12.2066 |
| net_avg_loss | -20.3143 |
| avg_hold_time_bars | 2.1085 |
| exposure | 0.1184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
