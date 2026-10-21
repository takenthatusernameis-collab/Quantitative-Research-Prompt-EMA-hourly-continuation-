# EMA Hourly Continuation — THETA/USDT P12_200

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8904 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0537 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -0.6070 |
| sortino_ratio | -0.1461 |
| max_drawdown | 0.3054 |
| cagr | -0.0675 |
| net_avg_win | 90.8802 |
| net_avg_loss | -107.2766 |
| avg_hold_time_bars | 58.7580 |
| exposure | 0.7505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
