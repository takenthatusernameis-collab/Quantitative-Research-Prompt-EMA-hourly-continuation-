# EMA Hourly Continuation — TFUEL/USDT P12_26

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.8174 |
| gross_win_rate | 0.4230 |
| sharpe_ratio | -5.3223 |
| sortino_ratio | -1.8042 |
| max_drawdown | 0.8803 |
| cagr | -0.5644 |
| net_avg_win | 44.6257 |
| net_avg_loss | -59.6220 |
| avg_hold_time_bars | 5.4885 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
