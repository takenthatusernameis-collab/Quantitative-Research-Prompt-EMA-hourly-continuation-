# EMA Hourly Continuation — IOTX/USDT P34_89

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5751 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -5.3087 |
| sortino_ratio | -1.9973 |
| max_drawdown | 0.9136 |
| cagr | -0.6182 |
| net_avg_win | 37.3537 |
| net_avg_loss | -55.6766 |
| avg_hold_time_bars | 7.5133 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
