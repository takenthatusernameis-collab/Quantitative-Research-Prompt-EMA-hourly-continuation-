# EMA Hourly Continuation — MNT/USDT P34_200

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6419 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.8987 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -2.0121 |
| sortino_ratio | -0.4722 |
| max_drawdown | 0.4801 |
| cagr | -0.2012 |
| net_avg_win | 58.0958 |
| net_avg_loss | -83.5944 |
| avg_hold_time_bars | 45.3177 |
| exposure | 0.5706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
