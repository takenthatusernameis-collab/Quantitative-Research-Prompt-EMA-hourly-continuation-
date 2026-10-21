# EMA Hourly Continuation — DOGE/USDT P20_26

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 147 |
| net_profit_factor | 0.5961 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8406 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -1.8669 |
| sortino_ratio | -0.3232 |
| max_drawdown | 0.3137 |
| cagr | -0.1382 |
| net_avg_win | 67.6320 |
| net_avg_loss | -97.6659 |
| avg_hold_time_bars | 4.5306 |
| exposure | 0.0303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
