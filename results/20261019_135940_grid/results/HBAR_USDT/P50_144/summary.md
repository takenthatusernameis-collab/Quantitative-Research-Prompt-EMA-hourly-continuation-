# EMA Hourly Continuation — HBAR/USDT P50_144

**Symbol:** HBAR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6211 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9998 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -3.5791 |
| sortino_ratio | -1.1096 |
| max_drawdown | 0.7488 |
| cagr | -0.4168 |
| net_avg_win | 51.9678 |
| net_avg_loss | -77.3851 |
| avg_hold_time_bars | 11.2053 |
| exposure | 0.2480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
