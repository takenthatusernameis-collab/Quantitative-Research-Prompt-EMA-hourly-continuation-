# EMA Hourly Continuation — DIA/USDT P21_55

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.6273 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -3.7283 |
| sortino_ratio | -1.2761 |
| max_drawdown | 0.7886 |
| cagr | -0.4439 |
| net_avg_win | 49.6278 |
| net_avg_loss | -64.9731 |
| avg_hold_time_bars | 7.8916 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
