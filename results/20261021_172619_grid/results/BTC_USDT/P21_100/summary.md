# EMA Hourly Continuation — BTC/USDT P21_100

**Symbol:** BTC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0628 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -2.4900 |
| sortino_ratio | -0.7274 |
| max_drawdown | 0.6179 |
| cagr | -0.2829 |
| net_avg_win | 53.7903 |
| net_avg_loss | -83.7373 |
| avg_hold_time_bars | 21.5139 |
| exposure | 0.4036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
