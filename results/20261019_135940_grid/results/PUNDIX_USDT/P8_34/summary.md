# EMA Hourly Continuation — PUNDIX/USDT P8_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1294 |
| net_profit_factor | 0.4409 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8657 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -8.3620 |
| sortino_ratio | -4.2295 |
| max_drawdown | 0.9949 |
| cagr | -0.8744 |
| net_avg_win | 13.4980 |
| net_avg_loss | -24.9478 |
| avg_hold_time_bars | 6.4977 |
| exposure | 0.3822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
