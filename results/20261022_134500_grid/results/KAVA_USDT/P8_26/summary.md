# EMA Hourly Continuation — KAVA/USDT P8_26

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1615 |
| net_profit_factor | 0.3745 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.8362 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -13.1716 |
| sortino_ratio | -7.4757 |
| max_drawdown | 0.9999 |
| cagr | -0.9791 |
| net_avg_win | 9.1524 |
| net_avg_loss | -16.6338 |
| avg_hold_time_bars | 4.2037 |
| exposure | 0.3086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
