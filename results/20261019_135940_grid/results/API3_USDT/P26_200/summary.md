# EMA Hourly Continuation — API3/USDT P26_200

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7001 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9595 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -2.2902 |
| sortino_ratio | -0.6420 |
| max_drawdown | 0.5725 |
| cagr | -0.2626 |
| net_avg_win | 65.6811 |
| net_avg_loss | -86.1161 |
| avg_hold_time_bars | 31.7154 |
| exposure | 0.5723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
