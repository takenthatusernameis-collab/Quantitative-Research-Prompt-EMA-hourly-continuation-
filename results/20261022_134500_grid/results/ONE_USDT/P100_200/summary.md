# EMA Hourly Continuation — ONE/USDT P100_200

**Symbol:** ONE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7091 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0524 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -2.1961 |
| sortino_ratio | -0.6025 |
| max_drawdown | 0.5210 |
| cagr | -0.2431 |
| net_avg_win | 66.2767 |
| net_avg_loss | -93.9791 |
| avg_hold_time_bars | 12.5068 |
| exposure | 0.2098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
