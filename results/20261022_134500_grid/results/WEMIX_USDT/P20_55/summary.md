# EMA Hourly Continuation — WEMIX/USDT P20_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1396 |
| net_profit_factor | 0.2121 |
| net_win_rate | 0.2908 |
| gross_profit_factor | 0.4394 |
| gross_win_rate | 0.3130 |
| sharpe_ratio | -16.8258 |
| sortino_ratio | -9.0981 |
| max_drawdown | 1.0000 |
| cagr | -0.9910 |
| net_avg_win | 6.6285 |
| net_avg_loss | -12.8193 |
| avg_hold_time_bars | 4.9678 |
| exposure | 0.3152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
