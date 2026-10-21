# EMA Hourly Continuation — FLOW/USDT P8_144

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8583 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -0.8361 |
| sortino_ratio | -0.2148 |
| max_drawdown | 0.2583 |
| cagr | -0.0964 |
| net_avg_win | 83.0113 |
| net_avg_loss | -100.3843 |
| avg_hold_time_bars | 51.9938 |
| exposure | 0.7610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
