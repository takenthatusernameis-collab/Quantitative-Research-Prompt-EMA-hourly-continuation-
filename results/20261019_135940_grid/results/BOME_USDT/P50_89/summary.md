# EMA Hourly Continuation — BOME/USDT P50_89

**Symbol:** BOME/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.5562 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -4.1121 |
| sortino_ratio | -1.5090 |
| max_drawdown | 0.8511 |
| cagr | -0.5154 |
| net_avg_win | 32.1130 |
| net_avg_loss | -54.0954 |
| avg_hold_time_bars | 4.9660 |
| exposure | 0.1526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
