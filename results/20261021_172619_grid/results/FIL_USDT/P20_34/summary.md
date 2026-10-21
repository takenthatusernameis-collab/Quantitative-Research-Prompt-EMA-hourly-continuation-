# EMA Hourly Continuation — FIL/USDT P20_34

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.6682 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.1418 |
| sortino_ratio | -0.5130 |
| max_drawdown | 0.4722 |
| cagr | -0.2088 |
| net_avg_win | 66.3330 |
| net_avg_loss | -93.0663 |
| avg_hold_time_bars | 5.1720 |
| exposure | 0.0656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
