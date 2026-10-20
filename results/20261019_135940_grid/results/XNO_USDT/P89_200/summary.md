# EMA Hourly Continuation — XNO/USDT P89_200

**Symbol:** XNO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.4896 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7579 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -5.5886 |
| sortino_ratio | -1.8536 |
| max_drawdown | 0.8915 |
| cagr | -0.5870 |
| net_avg_win | 37.6759 |
| net_avg_loss | -54.0774 |
| avg_hold_time_bars | 8.7709 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
