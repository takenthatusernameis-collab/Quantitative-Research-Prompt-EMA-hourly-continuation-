# EMA Hourly Continuation — GRAM/USDT P8_20

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1749 |
| net_profit_factor | 0.3128 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.8039 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -16.0839 |
| sortino_ratio | -9.6515 |
| max_drawdown | 1.0000 |
| cagr | -0.9940 |
| net_avg_win | 6.6753 |
| net_avg_loss | -13.6387 |
| avg_hold_time_bars | 2.5941 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
