# EMA Hourly Continuation — IOST/USDT P21_144

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0826 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -2.3203 |
| sortino_ratio | -0.7323 |
| max_drawdown | 0.6251 |
| cagr | -0.2974 |
| net_avg_win | 58.5923 |
| net_avg_loss | -86.0472 |
| avg_hold_time_bars | 23.0259 |
| exposure | 0.5254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
