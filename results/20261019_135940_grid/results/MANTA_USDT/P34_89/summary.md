# EMA Hourly Continuation — MANTA/USDT P34_89

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.5679 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8806 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -5.0775 |
| sortino_ratio | -1.8907 |
| max_drawdown | 0.9015 |
| cagr | -0.5998 |
| net_avg_win | 36.8321 |
| net_avg_loss | -54.2192 |
| avg_hold_time_bars | 7.4241 |
| exposure | 0.2379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
