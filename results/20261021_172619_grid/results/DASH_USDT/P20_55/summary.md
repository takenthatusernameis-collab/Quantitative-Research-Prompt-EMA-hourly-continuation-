# EMA Hourly Continuation — DASH/USDT P20_55

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6912 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9507 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -2.5559 |
| sortino_ratio | -0.8094 |
| max_drawdown | 0.6094 |
| cagr | -0.3097 |
| net_avg_win | 57.1986 |
| net_avg_loss | -77.5239 |
| avg_hold_time_bars | 8.9633 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
