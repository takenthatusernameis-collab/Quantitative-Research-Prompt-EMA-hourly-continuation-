# EMA Hourly Continuation — LPT/USDT P8_21

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1674 |
| net_profit_factor | 0.4640 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.8734 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -11.6088 |
| sortino_ratio | -6.6992 |
| max_drawdown | 0.9998 |
| cagr | -0.9652 |
| net_avg_win | 12.1205 |
| net_avg_loss | -19.4290 |
| avg_hold_time_bars | 3.0615 |
| exposure | 0.2330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
