# EMA Hourly Continuation — HBAR/USDT P20_26

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.2335 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.8237 |
| gross_win_rate | 0.4288 |
| sharpe_ratio | -14.6363 |
| sortino_ratio | -7.4429 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 6.7110 |
| net_avg_loss | -17.1438 |
| avg_hold_time_bars | 1.8634 |
| exposure | 0.1029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
