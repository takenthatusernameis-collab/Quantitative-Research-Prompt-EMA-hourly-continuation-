# EMA Hourly Continuation — VELO/USDT P12_21

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1531 |
| net_profit_factor | 0.4652 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8181 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -11.2315 |
| sortino_ratio | -6.2036 |
| max_drawdown | 0.9996 |
| cagr | -0.9556 |
| net_avg_win | 13.2726 |
| net_avg_loss | -21.3351 |
| avg_hold_time_bars | 2.2443 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
