# EMA Hourly Continuation — POPCAT/USDT P50_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7606 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -1.5721 |
| sortino_ratio | -0.4182 |
| max_drawdown | 0.3684 |
| cagr | -0.1759 |
| net_avg_win | 75.9375 |
| net_avg_loss | -90.3571 |
| avg_hold_time_bars | 20.0565 |
| exposure | 0.3189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
