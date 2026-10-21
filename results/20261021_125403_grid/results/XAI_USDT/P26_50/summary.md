# EMA Hourly Continuation — XAI/USDT P26_50

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7401 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9863 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.2212 |
| sortino_ratio | -0.6913 |
| max_drawdown | 0.5714 |
| cagr | -0.2711 |
| net_avg_win | 66.9761 |
| net_avg_loss | -88.2253 |
| avg_hold_time_bars | 6.6377 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
