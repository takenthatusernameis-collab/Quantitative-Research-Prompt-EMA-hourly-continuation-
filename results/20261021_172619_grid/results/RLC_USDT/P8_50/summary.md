# EMA Hourly Continuation — RLC/USDT P8_50

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 771 |
| net_profit_factor | 0.7537 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9724 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -2.7207 |
| sortino_ratio | -1.0793 |
| max_drawdown | 0.7340 |
| cagr | -0.3918 |
| net_avg_win | 57.8788 |
| net_avg_loss | -73.4821 |
| avg_hold_time_bars | 12.3541 |
| exposure | 0.4330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
