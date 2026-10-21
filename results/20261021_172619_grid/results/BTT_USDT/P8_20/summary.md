# EMA Hourly Continuation — BTT/USDT P8_20

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.4509 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.7899 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -6.9969 |
| sortino_ratio | -2.3476 |
| max_drawdown | 0.9402 |
| cagr | -0.6711 |
| net_avg_win | 35.1959 |
| net_avg_loss | -54.2714 |
| avg_hold_time_bars | 6.3596 |
| exposure | 0.1544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
