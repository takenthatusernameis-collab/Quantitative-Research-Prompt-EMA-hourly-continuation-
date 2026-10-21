# EMA Hourly Continuation — ONDO/USDT P8_89

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.8441 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9949 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.2354 |
| sortino_ratio | -0.4008 |
| max_drawdown | 0.5045 |
| cagr | -0.1710 |
| net_avg_win | 79.4131 |
| net_avg_loss | -93.3533 |
| avg_hold_time_bars | 24.3658 |
| exposure | 0.5693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
