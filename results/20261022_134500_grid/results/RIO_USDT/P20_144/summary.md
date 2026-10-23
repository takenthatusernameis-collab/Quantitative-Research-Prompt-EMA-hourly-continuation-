# EMA Hourly Continuation — RIO/USDT P20_144

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6462 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.8447 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -4.3238 |
| sortino_ratio | -1.5817 |
| max_drawdown | 0.8736 |
| cagr | -0.5314 |
| net_avg_win | 51.9853 |
| net_avg_loss | -63.4193 |
| avg_hold_time_bars | 16.8092 |
| exposure | 0.5217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
