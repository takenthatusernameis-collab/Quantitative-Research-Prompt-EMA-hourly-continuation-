# EMA Hourly Continuation — NEAR/USDT P20_144

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7890 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.3943 |
| sortino_ratio | -0.3764 |
| max_drawdown | 0.4264 |
| cagr | -0.1606 |
| net_avg_win | 76.8901 |
| net_avg_loss | -90.6372 |
| avg_hold_time_bars | 31.6630 |
| exposure | 0.5167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
