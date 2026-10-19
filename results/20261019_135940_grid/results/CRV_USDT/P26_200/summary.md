# EMA Hourly Continuation — CRV/USDT P26_200

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.6887 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -2.7035 |
| sortino_ratio | -0.7581 |
| max_drawdown | 0.6468 |
| cagr | -0.3054 |
| net_avg_win | 70.1699 |
| net_avg_loss | -92.1409 |
| avg_hold_time_bars | 31.8543 |
| exposure | 0.5763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
