# EMA Hourly Continuation — AMP/USDT P26_200

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.4303 |
| net_win_rate | 0.4159 |
| gross_profit_factor | 0.7087 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -5.8818 |
| sortino_ratio | -2.0685 |
| max_drawdown | 0.9253 |
| cagr | -0.6335 |
| net_avg_win | 26.5070 |
| net_avg_loss | -43.8612 |
| avg_hold_time_bars | 19.3190 |
| exposure | 0.5532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
