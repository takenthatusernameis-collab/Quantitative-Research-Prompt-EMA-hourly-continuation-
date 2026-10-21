# EMA Hourly Continuation — KSM/USDT P34_200

**Symbol:** KSM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8092 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0097 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.1311 |
| sortino_ratio | -0.2740 |
| max_drawdown | 0.3434 |
| cagr | -0.1196 |
| net_avg_win | 80.0592 |
| net_avg_loss | -101.0317 |
| avg_hold_time_bars | 40.3415 |
| exposure | 0.5263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
