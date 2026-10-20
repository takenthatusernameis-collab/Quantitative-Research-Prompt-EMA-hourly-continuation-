# EMA Hourly Continuation — ZRX/USDT P26_100

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6351 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -4.0042 |
| sortino_ratio | -1.4087 |
| max_drawdown | 0.8220 |
| cagr | -0.4884 |
| net_avg_win | 48.0360 |
| net_avg_loss | -68.2341 |
| avg_hold_time_bars | 12.8939 |
| exposure | 0.3645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
