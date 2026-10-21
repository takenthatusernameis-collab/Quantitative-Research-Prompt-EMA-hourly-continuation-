# EMA Hourly Continuation — ICP/USDT P20_21

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 88 |
| net_profit_factor | 0.9381 |
| net_win_rate | 0.5682 |
| gross_profit_factor | 1.3027 |
| gross_win_rate | 0.5682 |
| sharpe_ratio | -0.1585 |
| sortino_ratio | -0.0217 |
| max_drawdown | 0.0975 |
| cagr | -0.0111 |
| net_avg_win | 83.6356 |
| net_avg_loss | -117.3115 |
| avg_hold_time_bars | 3.8750 |
| exposure | 0.0155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
