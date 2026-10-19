# EMA Hourly Continuation — JTO/USDT P20_50

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.6288 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9996 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -4.9258 |
| sortino_ratio | -2.1811 |
| max_drawdown | 0.9281 |
| cagr | -0.6461 |
| net_avg_win | 32.9671 |
| net_avg_loss | -49.2231 |
| avg_hold_time_bars | 5.4771 |
| exposure | 0.2447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
