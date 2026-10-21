# EMA Hourly Continuation — MOVR/USDT P20_55

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.7631 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.1885 |
| sortino_ratio | -0.7506 |
| max_drawdown | 0.6378 |
| cagr | -0.2918 |
| net_avg_win | 65.9546 |
| net_avg_loss | -84.0584 |
| avg_hold_time_bars | 8.1969 |
| exposure | 0.2139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
