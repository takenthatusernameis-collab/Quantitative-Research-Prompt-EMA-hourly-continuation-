# EMA Hourly Continuation — MOCA/USDT P12_144

**Symbol:** MOCA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.6104 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -3.6501 |
| sortino_ratio | -1.0932 |
| max_drawdown | 0.7318 |
| cagr | -0.4149 |
| net_avg_win | 57.5220 |
| net_avg_loss | -79.7042 |
| avg_hold_time_bars | 32.3556 |
| exposure | 0.6796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
