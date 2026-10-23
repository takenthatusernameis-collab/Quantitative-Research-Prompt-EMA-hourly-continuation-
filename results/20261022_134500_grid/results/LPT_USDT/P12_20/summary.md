# EMA Hourly Continuation — LPT/USDT P12_20

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1503 |
| net_profit_factor | 0.4137 |
| net_win_rate | 0.4045 |
| gross_profit_factor | 0.8957 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -13.0135 |
| sortino_ratio | -7.1909 |
| max_drawdown | 0.9999 |
| cagr | -0.9741 |
| net_avg_win | 11.6033 |
| net_avg_loss | -19.0545 |
| avg_hold_time_bars | 2.4724 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
