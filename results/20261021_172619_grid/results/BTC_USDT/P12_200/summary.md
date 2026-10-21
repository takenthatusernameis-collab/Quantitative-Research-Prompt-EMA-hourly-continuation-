# EMA Hourly Continuation — BTC/USDT P12_200

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7848 |
| net_win_rate | 0.5249 |
| gross_profit_factor | 1.1041 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -1.1622 |
| sortino_ratio | -0.2718 |
| max_drawdown | 0.3227 |
| cagr | -0.1177 |
| net_avg_win | 69.3550 |
| net_avg_loss | -97.6417 |
| avg_hold_time_bars | 60.7907 |
| exposure | 0.7319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
