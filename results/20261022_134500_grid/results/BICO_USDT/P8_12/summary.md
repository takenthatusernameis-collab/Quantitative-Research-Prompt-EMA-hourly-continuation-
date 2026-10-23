# EMA Hourly Continuation — BICO/USDT P8_12

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.3289 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -12.7816 |
| sortino_ratio | -7.2468 |
| max_drawdown | 0.9999 |
| cagr | -0.9740 |
| net_avg_win | 7.4822 |
| net_avg_loss | -15.8172 |
| avg_hold_time_bars | 2.4972 |
| exposure | 0.1813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
