# EMA Hourly Continuation — KNC/USDT P20_26

**Symbol:** KNC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.2326 |
| net_win_rate | 0.3712 |
| gross_profit_factor | 0.8182 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -13.2480 |
| sortino_ratio | -6.3781 |
| max_drawdown | 0.9998 |
| cagr | -0.9640 |
| net_avg_win | 7.4267 |
| net_avg_loss | -18.8535 |
| avg_hold_time_bars | 3.1065 |
| exposure | 0.1552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
