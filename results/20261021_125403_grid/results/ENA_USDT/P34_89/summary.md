# EMA Hourly Continuation — ENA/USDT P34_89

**Symbol:** ENA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.8458 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0074 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.0012 |
| sortino_ratio | -0.2879 |
| max_drawdown | 0.3439 |
| cagr | -0.1261 |
| net_avg_win | 77.5932 |
| net_avg_loss | -93.1163 |
| avg_hold_time_bars | 10.9404 |
| exposure | 0.2004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
