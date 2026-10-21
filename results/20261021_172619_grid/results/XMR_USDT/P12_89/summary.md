# EMA Hourly Continuation — XMR/USDT P12_89

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.7053 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9195 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.6138 |
| sortino_ratio | -0.8837 |
| max_drawdown | 0.6510 |
| cagr | -0.3334 |
| net_avg_win | 57.0474 |
| net_avg_loss | -73.7314 |
| avg_hold_time_bars | 16.0605 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
