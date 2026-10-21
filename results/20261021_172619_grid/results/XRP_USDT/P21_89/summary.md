# EMA Hourly Continuation — XRP/USDT P21_89

**Symbol:** XRP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6399 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9080 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -2.9152 |
| sortino_ratio | -0.8948 |
| max_drawdown | 0.6785 |
| cagr | -0.3356 |
| net_avg_win | 51.8541 |
| net_avg_loss | -73.9692 |
| avg_hold_time_bars | 15.2408 |
| exposure | 0.3194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
