# EMA Hourly Continuation — XRP/USDT P89_144

**Symbol:** XRP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7431 |
| net_win_rate | 0.5395 |
| gross_profit_factor | 1.1637 |
| gross_win_rate | 0.5395 |
| sharpe_ratio | -1.3426 |
| sortino_ratio | -0.2935 |
| max_drawdown | 0.3099 |
| cagr | -0.1253 |
| net_avg_win | 67.1503 |
| net_avg_loss | -105.8497 |
| avg_hold_time_bars | 7.3860 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
