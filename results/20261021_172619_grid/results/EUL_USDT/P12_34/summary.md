# EMA Hourly Continuation — EUL/USDT P12_34

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.6053 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8122 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -3.5161 |
| sortino_ratio | -1.2448 |
| max_drawdown | 0.7701 |
| cagr | -0.4357 |
| net_avg_win | 41.1655 |
| net_avg_loss | -57.6534 |
| avg_hold_time_bars | 7.8465 |
| exposure | 0.2208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
