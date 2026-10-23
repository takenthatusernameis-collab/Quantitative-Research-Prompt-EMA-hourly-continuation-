# EMA Hourly Continuation — DEXE/USDT P8_20

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1635 |
| net_profit_factor | 0.2377 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.5565 |
| gross_win_rate | 0.4190 |
| sharpe_ratio | -13.5843 |
| sortino_ratio | -7.7941 |
| max_drawdown | 1.0000 |
| cagr | -0.9813 |
| net_avg_win | 4.8566 |
| net_avg_loss | -13.2099 |
| avg_hold_time_bars | 4.3211 |
| exposure | 0.3211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
