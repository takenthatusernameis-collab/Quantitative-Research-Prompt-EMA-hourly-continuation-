# EMA Hourly Continuation — XCN/USDT P26_89

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 827 |
| net_profit_factor | 0.4063 |
| net_win_rate | 0.4111 |
| gross_profit_factor | 0.7591 |
| gross_win_rate | 0.4220 |
| sharpe_ratio | -8.0661 |
| sortino_ratio | -3.2327 |
| max_drawdown | 0.9846 |
| cagr | -0.8090 |
| net_avg_win | 19.8122 |
| net_avg_loss | -34.0443 |
| avg_hold_time_bars | 9.2576 |
| exposure | 0.3480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
