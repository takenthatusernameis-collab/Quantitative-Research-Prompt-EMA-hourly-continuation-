# EMA Hourly Continuation — ILV/USDT P26_100

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8146 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0341 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.5216 |
| sortino_ratio | -0.4781 |
| max_drawdown | 0.4830 |
| cagr | -0.1982 |
| net_avg_win | 76.9800 |
| net_avg_loss | -96.8954 |
| avg_hold_time_bars | 16.0417 |
| exposure | 0.3500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
