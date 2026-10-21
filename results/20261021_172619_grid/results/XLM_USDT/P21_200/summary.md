# EMA Hourly Continuation — XLM/USDT P21_200

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7945 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0277 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.1921 |
| sortino_ratio | -0.2923 |
| max_drawdown | 0.3302 |
| cagr | -0.1265 |
| net_avg_win | 74.7019 |
| net_avg_loss | -97.2880 |
| avg_hold_time_bars | 46.1092 |
| exposure | 0.6141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
