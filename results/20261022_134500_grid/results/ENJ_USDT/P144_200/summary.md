# EMA Hourly Continuation — ENJ/USDT P144_200

**Symbol:** ENJ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.5654 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0000 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -3.1506 |
| sortino_ratio | -0.8727 |
| max_drawdown | 0.6504 |
| cagr | -0.3381 |
| net_avg_win | 45.0009 |
| net_avg_loss | -77.5173 |
| avg_hold_time_bars | 4.9657 |
| exposure | 0.0852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
