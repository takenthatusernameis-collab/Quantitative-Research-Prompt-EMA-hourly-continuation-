# EMA Hourly Continuation — ZRX/USDT P26_200

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.6031 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8491 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.2059 |
| sortino_ratio | -0.8934 |
| max_drawdown | 0.6767 |
| cagr | -0.3481 |
| net_avg_win | 56.2161 |
| net_avg_loss | -77.1724 |
| avg_hold_time_bars | 31.5802 |
| exposure | 0.5641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
