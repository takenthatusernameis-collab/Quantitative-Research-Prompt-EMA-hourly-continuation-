# EMA Hourly Continuation — XTZ/USDT P20_34

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5879 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -3.5013 |
| sortino_ratio | -1.0266 |
| max_drawdown | 0.7073 |
| cagr | -0.3751 |
| net_avg_win | 50.4278 |
| net_avg_loss | -76.4218 |
| avg_hold_time_bars | 5.1947 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
