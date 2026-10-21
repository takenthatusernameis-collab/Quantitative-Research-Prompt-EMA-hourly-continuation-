# EMA Hourly Continuation — WIF/USDT P8_20

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8302 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0363 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.2833 |
| sortino_ratio | -0.3843 |
| max_drawdown | 0.4123 |
| cagr | -0.1632 |
| net_avg_win | 79.8004 |
| net_avg_loss | -99.2691 |
| avg_hold_time_bars | 5.5655 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
