# EMA Hourly Continuation — AVAX/USDT P12_21

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1426 |
| net_profit_factor | 0.3125 |
| net_win_rate | 0.3955 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -14.0369 |
| sortino_ratio | -7.6221 |
| max_drawdown | 1.0000 |
| cagr | -0.9816 |
| net_avg_win | 8.0577 |
| net_avg_loss | -16.8725 |
| avg_hold_time_bars | 2.2426 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
