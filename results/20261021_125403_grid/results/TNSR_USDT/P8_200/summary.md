# EMA Hourly Continuation — TNSR/USDT P8_200

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7879 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9220 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -1.4722 |
| sortino_ratio | -0.3768 |
| max_drawdown | 0.4013 |
| cagr | -0.1601 |
| net_avg_win | 85.3144 |
| net_avg_loss | -98.1504 |
| avg_hold_time_bars | 52.1258 |
| exposure | 0.7690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
