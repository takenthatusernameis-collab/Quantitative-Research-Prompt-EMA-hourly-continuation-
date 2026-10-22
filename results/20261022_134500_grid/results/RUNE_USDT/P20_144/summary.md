# EMA Hourly Continuation — RUNE/USDT P20_144

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7761 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0874 |
| gross_win_rate | 0.5246 |
| sharpe_ratio | -1.4625 |
| sortino_ratio | -0.3990 |
| max_drawdown | 0.4132 |
| cagr | -0.1710 |
| net_avg_win | 68.5370 |
| net_avg_loss | -95.3308 |
| avg_hold_time_bars | 39.1066 |
| exposure | 0.6506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
