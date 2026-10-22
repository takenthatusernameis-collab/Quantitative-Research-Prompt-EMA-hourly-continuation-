# EMA Hourly Continuation — RUNE/USDT P12_50

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.5970 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -6.0200 |
| sortino_ratio | -2.6648 |
| max_drawdown | 0.9635 |
| cagr | -0.7285 |
| net_avg_win | 29.5102 |
| net_avg_loss | -46.2694 |
| avg_hold_time_bars | 8.2052 |
| exposure | 0.3726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
