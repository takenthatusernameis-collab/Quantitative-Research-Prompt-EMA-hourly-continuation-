# EMA Hourly Continuation — HBAR/USDT P8_89

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.6320 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9877 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -4.3826 |
| sortino_ratio | -1.7488 |
| max_drawdown | 0.8906 |
| cagr | -0.5697 |
| net_avg_win | 38.9283 |
| net_avg_loss | -57.7313 |
| avg_hold_time_bars | 16.7968 |
| exposure | 0.6123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
