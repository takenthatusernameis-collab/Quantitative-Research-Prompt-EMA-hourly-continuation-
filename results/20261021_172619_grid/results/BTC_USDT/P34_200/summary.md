# EMA Hourly Continuation — BTC/USDT P34_200

**Symbol:** BTC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6749 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0184 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -2.1437 |
| sortino_ratio | -0.5154 |
| max_drawdown | 0.4962 |
| cagr | -0.2116 |
| net_avg_win | 63.9333 |
| net_avg_loss | -92.9821 |
| avg_hold_time_bars | 36.6006 |
| exposure | 0.4729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
