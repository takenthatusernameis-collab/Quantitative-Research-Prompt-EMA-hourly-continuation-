# EMA Hourly Continuation — ZIL/USDT P21_89

**Symbol:** ZIL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8319 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.0969 |
| gross_win_rate | 0.5194 |
| sharpe_ratio | -1.4067 |
| sortino_ratio | -0.4476 |
| max_drawdown | 0.5201 |
| cagr | -0.1868 |
| net_avg_win | 78.9303 |
| net_avg_loss | -102.5456 |
| avg_hold_time_bars | 15.2249 |
| exposure | 0.3384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
