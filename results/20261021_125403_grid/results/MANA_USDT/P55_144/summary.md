# EMA Hourly Continuation — MANA/USDT P55_144

**Symbol:** MANA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -1.8616 |
| sortino_ratio | -0.4868 |
| max_drawdown | 0.4401 |
| cagr | -0.2007 |
| net_avg_win | 69.5937 |
| net_avg_loss | -90.0429 |
| avg_hold_time_bars | 16.7284 |
| exposure | 0.2547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
