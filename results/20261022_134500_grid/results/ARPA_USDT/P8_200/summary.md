# EMA Hourly Continuation — ARPA/USDT P8_200

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8822 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.4766 |
| sortino_ratio | -1.0864 |
| max_drawdown | 0.7392 |
| cagr | -0.4034 |
| net_avg_win | 49.1027 |
| net_avg_loss | -69.6502 |
| avg_hold_time_bars | 33.6505 |
| exposure | 0.7537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
