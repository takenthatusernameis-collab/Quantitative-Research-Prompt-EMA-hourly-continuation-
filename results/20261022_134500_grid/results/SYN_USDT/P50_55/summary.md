# EMA Hourly Continuation — SYN/USDT P50_55

**Symbol:** SYN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.2063 |
| net_win_rate | 0.3799 |
| gross_profit_factor | 0.6230 |
| gross_win_rate | 0.4187 |
| sharpe_ratio | -10.7460 |
| sortino_ratio | -4.4037 |
| max_drawdown | 0.9972 |
| cagr | -0.9035 |
| net_avg_win | 8.2789 |
| net_avg_loss | -24.5854 |
| avg_hold_time_bars | 2.4223 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
