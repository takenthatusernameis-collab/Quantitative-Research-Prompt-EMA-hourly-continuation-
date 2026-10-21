# EMA Hourly Continuation — EWT/USDT P20_50

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.6564 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8615 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.8266 |
| sortino_ratio | -0.8240 |
| max_drawdown | 0.6175 |
| cagr | -0.3155 |
| net_avg_win | 60.7655 |
| net_avg_loss | -78.7119 |
| avg_hold_time_bars | 8.5286 |
| exposure | 0.1628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
