# EMA Hourly Continuation — ANKR/USDT P26_89

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.5157 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -6.1620 |
| sortino_ratio | -2.3108 |
| max_drawdown | 0.9444 |
| cagr | -0.6795 |
| net_avg_win | 32.1714 |
| net_avg_loss | -48.0572 |
| avg_hold_time_bars | 10.6346 |
| exposure | 0.3466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
