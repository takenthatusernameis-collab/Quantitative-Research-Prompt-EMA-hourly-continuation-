# EMA Hourly Continuation — LINK/USDT P8_26

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.7471 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0184 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -2.3749 |
| sortino_ratio | -0.8357 |
| max_drawdown | 0.6677 |
| cagr | -0.3179 |
| net_avg_win | 60.3781 |
| net_avg_loss | -81.9057 |
| avg_hold_time_bars | 6.8700 |
| exposure | 0.1874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
