# EMA Hourly Continuation — MANTA/USDT P21_144

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.8173 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.1527 |
| sortino_ratio | -0.2992 |
| max_drawdown | 0.3000 |
| cagr | -0.1297 |
| net_avg_win | 81.3633 |
| net_avg_loss | -95.9928 |
| avg_hold_time_bars | 39.4515 |
| exposure | 0.5918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
