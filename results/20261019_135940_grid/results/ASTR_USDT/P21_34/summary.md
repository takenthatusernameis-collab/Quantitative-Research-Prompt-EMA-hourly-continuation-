# EMA Hourly Continuation — ASTR/USDT P21_34

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.3707 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -9.5071 |
| sortino_ratio | -4.2834 |
| max_drawdown | 0.9958 |
| cagr | -0.8853 |
| net_avg_win | 13.4825 |
| net_avg_loss | -27.4696 |
| avg_hold_time_bars | 3.3442 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
