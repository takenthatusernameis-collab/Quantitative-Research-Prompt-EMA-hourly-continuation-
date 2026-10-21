# EMA Hourly Continuation — SKY/USDT P20_55

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9112 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.2081 |
| sortino_ratio | -1.1025 |
| max_drawdown | 0.6578 |
| cagr | -0.3979 |
| net_avg_win | 53.7401 |
| net_avg_loss | -75.6306 |
| avg_hold_time_bars | 8.8602 |
| exposure | 0.2332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
