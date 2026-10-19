# EMA Hourly Continuation — ETC/USDT P21_34

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1166 |
| net_profit_factor | 0.2770 |
| net_win_rate | 0.3791 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4288 |
| sharpe_ratio | -13.6463 |
| sortino_ratio | -6.7729 |
| max_drawdown | 0.9999 |
| cagr | -0.9709 |
| net_avg_win | 8.6659 |
| net_avg_loss | -19.1007 |
| avg_hold_time_bars | 2.2581 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
