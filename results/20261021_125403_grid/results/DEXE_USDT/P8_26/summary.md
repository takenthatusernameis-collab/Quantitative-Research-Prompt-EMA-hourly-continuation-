# EMA Hourly Continuation — DEXE/USDT P8_26

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.7007 |
| net_win_rate | 0.4992 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -2.4535 |
| sortino_ratio | -0.8747 |
| max_drawdown | 0.6492 |
| cagr | -0.3314 |
| net_avg_win | 48.1928 |
| net_avg_loss | -68.5573 |
| avg_hold_time_bars | 10.5929 |
| exposure | 0.2980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
