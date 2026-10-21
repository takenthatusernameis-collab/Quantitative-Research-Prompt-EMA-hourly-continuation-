# EMA Hourly Continuation — KSM/USDT P50_55

**Symbol:** KSM/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 146 |
| net_profit_factor | 0.6272 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -1.7274 |
| sortino_ratio | -0.3002 |
| max_drawdown | 0.2994 |
| cagr | -0.1277 |
| net_avg_win | 68.8300 |
| net_avg_loss | -103.8885 |
| avg_hold_time_bars | 4.2877 |
| exposure | 0.0285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
