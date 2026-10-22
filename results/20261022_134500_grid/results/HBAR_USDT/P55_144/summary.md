# EMA Hourly Continuation — HBAR/USDT P55_144

**Symbol:** HBAR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6163 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.8495 |
| sortino_ratio | -1.2122 |
| max_drawdown | 0.7771 |
| cagr | -0.4439 |
| net_avg_win | 52.2454 |
| net_avg_loss | -76.3919 |
| avg_hold_time_bars | 9.7920 |
| exposure | 0.2225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
