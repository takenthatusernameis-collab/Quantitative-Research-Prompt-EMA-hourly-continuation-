# EMA Hourly Continuation — QI/USDT P34_55

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.4786 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9764 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -6.8374 |
| sortino_ratio | -2.7711 |
| max_drawdown | 0.9692 |
| cagr | -0.7421 |
| net_avg_win | 23.3005 |
| net_avg_loss | -42.2549 |
| avg_hold_time_bars | 3.4744 |
| exposure | 0.1289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
