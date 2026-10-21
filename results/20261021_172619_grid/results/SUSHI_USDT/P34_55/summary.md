# EMA Hourly Continuation — SUSHI/USDT P34_55

**Symbol:** SUSHI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6322 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8830 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.8484 |
| sortino_ratio | -0.7662 |
| max_drawdown | 0.6023 |
| cagr | -0.2955 |
| net_avg_win | 61.1230 |
| net_avg_loss | -83.5168 |
| avg_hold_time_bars | 5.6208 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
