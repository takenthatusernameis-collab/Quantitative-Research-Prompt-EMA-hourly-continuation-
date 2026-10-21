# EMA Hourly Continuation — BNB/USDT P8_12

**Symbol:** BNB/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.7141 |
| net_win_rate | 0.5735 |
| gross_profit_factor | 1.3360 |
| gross_win_rate | 0.5735 |
| sharpe_ratio | -1.4164 |
| sortino_ratio | -0.2955 |
| max_drawdown | 0.2843 |
| cagr | -0.1247 |
| net_avg_win | 60.6800 |
| net_avg_loss | -114.2823 |
| avg_hold_time_bars | 4.6716 |
| exposure | 0.0433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
