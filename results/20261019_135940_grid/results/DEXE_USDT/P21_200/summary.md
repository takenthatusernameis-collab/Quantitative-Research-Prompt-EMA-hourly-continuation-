# EMA Hourly Continuation — DEXE/USDT P21_200

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.8209 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0923 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -0.9126 |
| sortino_ratio | -0.2304 |
| max_drawdown | 0.3890 |
| cagr | -0.1037 |
| net_avg_win | 68.0371 |
| net_avg_loss | -88.9158 |
| avg_hold_time_bars | 49.6581 |
| exposure | 0.7065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
