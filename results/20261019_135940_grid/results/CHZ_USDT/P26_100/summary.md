# EMA Hourly Continuation — CHZ/USDT P26_100

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.5700 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -4.3466 |
| sortino_ratio | -1.5060 |
| max_drawdown | 0.8472 |
| cagr | -0.5237 |
| net_avg_win | 38.2191 |
| net_avg_loss | -61.0101 |
| avg_hold_time_bars | 12.6033 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
