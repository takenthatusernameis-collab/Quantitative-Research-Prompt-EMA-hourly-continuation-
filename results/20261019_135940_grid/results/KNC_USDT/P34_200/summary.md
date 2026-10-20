# EMA Hourly Continuation — KNC/USDT P34_200

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7713 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1712 |
| gross_win_rate | 0.5392 |
| sharpe_ratio | -1.4994 |
| sortino_ratio | -0.3837 |
| max_drawdown | 0.4447 |
| cagr | -0.1695 |
| net_avg_win | 71.0503 |
| net_avg_loss | -105.1885 |
| avg_hold_time_bars | 37.4006 |
| exposure | 0.5644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
