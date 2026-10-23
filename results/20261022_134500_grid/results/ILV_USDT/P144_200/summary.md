# EMA Hourly Continuation — ILV/USDT P144_200

**Symbol:** ILV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5115 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -3.5589 |
| sortino_ratio | -0.9471 |
| max_drawdown | 0.6855 |
| cagr | -0.3691 |
| net_avg_win | 42.9856 |
| net_avg_loss | -74.6454 |
| avg_hold_time_bars | 5.0704 |
| exposure | 0.0818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
