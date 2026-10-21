# EMA Hourly Continuation — MANA/USDT P21_144

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.8250 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0066 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.1501 |
| sortino_ratio | -0.3114 |
| max_drawdown | 0.3329 |
| cagr | -0.1349 |
| net_avg_win | 79.8964 |
| net_avg_loss | -97.9322 |
| avg_hold_time_bars | 33.8324 |
| exposure | 0.5505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
