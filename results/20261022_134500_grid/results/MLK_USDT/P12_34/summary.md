# EMA Hourly Continuation — MLK/USDT P12_34

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1570 |
| net_profit_factor | 0.2311 |
| net_win_rate | 0.2662 |
| gross_profit_factor | 0.5462 |
| gross_win_rate | 0.2822 |
| sharpe_ratio | -18.8251 |
| sortino_ratio | -10.7735 |
| max_drawdown | 1.0000 |
| cagr | -0.9963 |
| net_avg_win | 7.1916 |
| net_avg_loss | -11.2900 |
| avg_hold_time_bars | 3.8822 |
| exposure | 0.2758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
