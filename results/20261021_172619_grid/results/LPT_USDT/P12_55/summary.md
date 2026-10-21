# EMA Hourly Continuation — LPT/USDT P12_55

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.7514 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9528 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.6634 |
| sortino_ratio | -0.9712 |
| max_drawdown | 0.6928 |
| cagr | -0.3612 |
| net_avg_win | 64.8182 |
| net_avg_loss | -80.1543 |
| avg_hold_time_bars | 12.7829 |
| exposure | 0.3800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
