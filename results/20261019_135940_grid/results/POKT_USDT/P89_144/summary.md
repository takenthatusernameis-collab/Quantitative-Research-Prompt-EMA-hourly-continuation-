# EMA Hourly Continuation — POKT/USDT P89_144

**Symbol:** POKT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.4366 |
| net_win_rate | 0.3876 |
| gross_profit_factor | 0.7371 |
| gross_win_rate | 0.3993 |
| sharpe_ratio | -6.8356 |
| sortino_ratio | -2.3625 |
| max_drawdown | 0.9437 |
| cagr | -0.6793 |
| net_avg_win | 31.6438 |
| net_avg_loss | -45.8681 |
| avg_hold_time_bars | 5.7768 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
