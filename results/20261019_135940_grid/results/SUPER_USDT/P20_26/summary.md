# EMA Hourly Continuation — SUPER/USDT P20_26

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.2959 |
| net_win_rate | 0.3963 |
| gross_profit_factor | 0.7896 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -12.5448 |
| sortino_ratio | -6.1981 |
| max_drawdown | 0.9997 |
| cagr | -0.9615 |
| net_avg_win | 8.8645 |
| net_avg_loss | -19.6661 |
| avg_hold_time_bars | 2.1196 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
