# EMA Hourly Continuation — JASMY/USDT P12_21

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1492 |
| net_profit_factor | 0.3614 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.7487 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -12.2909 |
| sortino_ratio | -6.7462 |
| max_drawdown | 0.9998 |
| cagr | -0.9681 |
| net_avg_win | 8.9530 |
| net_avg_loss | -18.2053 |
| avg_hold_time_bars | 2.1830 |
| exposure | 0.1480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
