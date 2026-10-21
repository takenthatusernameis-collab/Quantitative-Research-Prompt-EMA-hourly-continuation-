# EMA Hourly Continuation — WIN/USDT P20_21

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 126 |
| net_profit_factor | 0.7258 |
| net_win_rate | 0.5476 |
| gross_profit_factor | 1.2108 |
| gross_win_rate | 0.5476 |
| sharpe_ratio | -1.0887 |
| sortino_ratio | -0.1777 |
| max_drawdown | 0.2165 |
| cagr | -0.0775 |
| net_avg_win | 70.3304 |
| net_avg_loss | -117.3033 |
| avg_hold_time_bars | 4.6587 |
| exposure | 0.0267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
