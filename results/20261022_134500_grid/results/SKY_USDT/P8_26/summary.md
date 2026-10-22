# EMA Hourly Continuation — SKY/USDT P8_26

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.4208 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8700 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -9.9397 |
| sortino_ratio | -5.3681 |
| max_drawdown | 0.9956 |
| cagr | -0.9290 |
| net_avg_win | 13.6202 |
| net_avg_loss | -26.0422 |
| avg_hold_time_bars | 4.0647 |
| exposure | 0.2699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
