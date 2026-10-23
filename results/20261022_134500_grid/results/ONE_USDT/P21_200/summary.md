# EMA Hourly Continuation — ONE/USDT P21_200

**Symbol:** ONE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7043 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -2.2422 |
| sortino_ratio | -0.5904 |
| max_drawdown | 0.5151 |
| cagr | -0.2405 |
| net_avg_win | 73.8067 |
| net_avg_loss | -91.6890 |
| avg_hold_time_bars | 42.8290 |
| exposure | 0.6716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
