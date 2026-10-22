# EMA Hourly Continuation — XRP/USDT P21_89

**Symbol:** XRP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.4193 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8932 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -7.3620 |
| sortino_ratio | -2.8159 |
| max_drawdown | 0.9751 |
| cagr | -0.7608 |
| net_avg_win | 21.9476 |
| net_avg_loss | -39.1308 |
| avg_hold_time_bars | 10.1324 |
| exposure | 0.3445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
