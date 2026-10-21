# EMA Hourly Continuation — XRP/USDT P55_89

**Symbol:** XRP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.6205 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9887 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2440 |
| sortino_ratio | -0.5050 |
| max_drawdown | 0.4549 |
| cagr | -0.2053 |
| net_avg_win | 58.7609 |
| net_avg_loss | -94.7055 |
| avg_hold_time_bars | 7.5287 |
| exposure | 0.0835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
