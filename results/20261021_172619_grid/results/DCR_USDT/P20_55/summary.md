# EMA Hourly Continuation — DCR/USDT P20_55

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.5988 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.8417 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -3.5161 |
| sortino_ratio | -1.2272 |
| max_drawdown | 0.7759 |
| cagr | -0.4327 |
| net_avg_win | 40.2525 |
| net_avg_loss | -59.2430 |
| avg_hold_time_bars | 8.2691 |
| exposure | 0.2253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
