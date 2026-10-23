# EMA Hourly Continuation — AGLD/USDT P21_55

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.5351 |
| net_win_rate | 0.4362 |
| gross_profit_factor | 0.8734 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -6.6606 |
| sortino_ratio | -2.8762 |
| max_drawdown | 0.9703 |
| cagr | -0.7474 |
| net_avg_win | 27.2014 |
| net_avg_loss | -39.3239 |
| avg_hold_time_bars | 6.3394 |
| exposure | 0.2697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
