# EMA Hourly Continuation — JUP/USDT P21_26

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 153 |
| net_profit_factor | 0.9561 |
| net_win_rate | 0.5621 |
| gross_profit_factor | 1.2733 |
| gross_win_rate | 0.5621 |
| sharpe_ratio | -0.1461 |
| sortino_ratio | -0.0263 |
| max_drawdown | 0.1451 |
| cagr | -0.0143 |
| net_avg_win | 89.8388 |
| net_avg_loss | -120.6157 |
| avg_hold_time_bars | 4.3725 |
| exposure | 0.0304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
