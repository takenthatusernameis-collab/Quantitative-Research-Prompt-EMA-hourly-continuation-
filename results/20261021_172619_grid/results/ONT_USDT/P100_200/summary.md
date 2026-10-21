# EMA Hourly Continuation — ONT/USDT P100_200

**Symbol:** ONT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.6572 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8544 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -2.2586 |
| sortino_ratio | -0.5409 |
| max_drawdown | 0.4817 |
| cagr | -0.2208 |
| net_avg_win | 68.3624 |
| net_avg_loss | -88.4795 |
| avg_hold_time_bars | 12.1930 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
