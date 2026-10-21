# EMA Hourly Continuation — TURBO/USDT P50_55

**Symbol:** TURBO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 83 |
| net_profit_factor | 0.8687 |
| net_win_rate | 0.5542 |
| gross_profit_factor | 1.2280 |
| gross_win_rate | 0.5542 |
| sharpe_ratio | -0.4076 |
| sortino_ratio | -0.0592 |
| max_drawdown | 0.1633 |
| cagr | -0.0272 |
| net_avg_win | 80.5353 |
| net_avg_loss | -115.2577 |
| avg_hold_time_bars | 5.0241 |
| exposure | 0.0227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
