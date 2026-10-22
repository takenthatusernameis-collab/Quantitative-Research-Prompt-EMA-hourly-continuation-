# EMA Hourly Continuation — VET/USDT P100_200

**Symbol:** VET/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.5392 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9492 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.5438 |
| sortino_ratio | -0.9638 |
| max_drawdown | 0.6929 |
| cagr | -0.3692 |
| net_avg_win | 47.1867 |
| net_avg_loss | -75.1403 |
| avg_hold_time_bars | 10.1440 |
| exposure | 0.1697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
