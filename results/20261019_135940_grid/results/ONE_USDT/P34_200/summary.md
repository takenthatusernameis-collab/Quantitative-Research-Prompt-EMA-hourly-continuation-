# EMA Hourly Continuation — ONE/USDT P34_200

**Symbol:** ONE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7235 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -2.1318 |
| sortino_ratio | -0.5936 |
| max_drawdown | 0.5208 |
| cagr | -0.2428 |
| net_avg_win | 70.7272 |
| net_avg_loss | -90.9083 |
| avg_hold_time_bars | 29.3031 |
| exposure | 0.5141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
