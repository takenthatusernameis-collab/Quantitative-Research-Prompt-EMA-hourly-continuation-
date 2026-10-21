# EMA Hourly Continuation — KMNO/USDT P26_144

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8230 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.1638 |
| sortino_ratio | -0.3168 |
| max_drawdown | 0.3505 |
| cagr | -0.1377 |
| net_avg_win | 79.6555 |
| net_avg_loss | -97.3332 |
| avg_hold_time_bars | 26.2325 |
| exposure | 0.4324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
