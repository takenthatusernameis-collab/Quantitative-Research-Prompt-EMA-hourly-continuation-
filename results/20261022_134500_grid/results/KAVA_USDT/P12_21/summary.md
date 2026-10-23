# EMA Hourly Continuation — KAVA/USDT P12_21

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1500 |
| net_profit_factor | 0.2450 |
| net_win_rate | 0.3767 |
| gross_profit_factor | 0.7081 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -15.3753 |
| sortino_ratio | -8.5933 |
| max_drawdown | 1.0000 |
| cagr | -0.9894 |
| net_avg_win | 5.7436 |
| net_avg_loss | -14.1658 |
| avg_hold_time_bars | 2.9633 |
| exposure | 0.2020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
