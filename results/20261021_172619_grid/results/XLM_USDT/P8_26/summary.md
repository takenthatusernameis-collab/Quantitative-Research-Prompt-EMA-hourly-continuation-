# EMA Hourly Continuation — XLM/USDT P8_26

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.7091 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0579 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -2.6267 |
| sortino_ratio | -0.9440 |
| max_drawdown | 0.6716 |
| cagr | -0.3498 |
| net_avg_win | 50.4947 |
| net_avg_loss | -74.9703 |
| avg_hold_time_bars | 6.6752 |
| exposure | 0.1887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
