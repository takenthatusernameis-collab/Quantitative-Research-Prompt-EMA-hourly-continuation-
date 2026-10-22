# EMA Hourly Continuation — XMR/USDT P55_144

**Symbol:** XMR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.3594 |
| net_win_rate | 0.4111 |
| gross_profit_factor | 0.7559 |
| gross_win_rate | 0.4199 |
| sharpe_ratio | -8.3161 |
| sortino_ratio | -3.3130 |
| max_drawdown | 0.9847 |
| cagr | -0.8098 |
| net_avg_win | 16.9419 |
| net_avg_loss | -32.9086 |
| avg_hold_time_bars | 6.6280 |
| exposure | 0.2389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
