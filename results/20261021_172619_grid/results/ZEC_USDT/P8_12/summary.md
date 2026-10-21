# EMA Hourly Continuation — ZEC/USDT P8_12

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.8832 |
| net_win_rate | 0.5435 |
| gross_profit_factor | 1.1696 |
| gross_win_rate | 0.5435 |
| sharpe_ratio | -0.4432 |
| sortino_ratio | -0.0871 |
| max_drawdown | 0.1924 |
| cagr | -0.0408 |
| net_avg_win | 75.1725 |
| net_avg_loss | -101.3205 |
| avg_hold_time_bars | 4.2391 |
| exposure | 0.0355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
