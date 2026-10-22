# EMA Hourly Continuation — KCS/USDT P8_50

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.2076 |
| net_win_rate | 0.3460 |
| gross_profit_factor | 0.5728 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -13.1772 |
| sortino_ratio | -6.1430 |
| max_drawdown | 0.9997 |
| cagr | -0.9621 |
| net_avg_win | 7.2142 |
| net_avg_loss | -18.3908 |
| avg_hold_time_bars | 10.2431 |
| exposure | 0.4884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
