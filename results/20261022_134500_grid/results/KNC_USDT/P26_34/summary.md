# EMA Hourly Continuation — KNC/USDT P26_34

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 989 |
| net_profit_factor | 0.2611 |
| net_win_rate | 0.3893 |
| gross_profit_factor | 0.8223 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -11.9644 |
| sortino_ratio | -5.4750 |
| max_drawdown | 0.9992 |
| cagr | -0.9410 |
| net_avg_win | 9.1728 |
| net_avg_loss | -22.3897 |
| avg_hold_time_bars | 3.1062 |
| exposure | 0.1396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
