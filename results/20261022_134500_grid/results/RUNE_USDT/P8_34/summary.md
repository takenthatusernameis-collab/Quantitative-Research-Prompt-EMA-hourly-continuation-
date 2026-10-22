# EMA Hourly Continuation — RUNE/USDT P8_34

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1335 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 1.0274 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -8.6038 |
| sortino_ratio | -4.3769 |
| max_drawdown | 0.9963 |
| cagr | -0.8908 |
| net_avg_win | 19.7566 |
| net_avg_loss | -30.5711 |
| avg_hold_time_bars | 5.4697 |
| exposure | 0.3319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
