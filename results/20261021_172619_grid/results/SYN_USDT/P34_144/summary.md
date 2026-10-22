# EMA Hourly Continuation — SYN/USDT P34_144

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9840 |
| net_win_rate | 0.5405 |
| gross_profit_factor | 1.1652 |
| gross_win_rate | 0.5405 |
| sharpe_ratio | -0.0421 |
| sortino_ratio | -0.0113 |
| max_drawdown | 0.1708 |
| cagr | -0.0118 |
| net_avg_win | 96.4718 |
| net_avg_loss | -115.3095 |
| avg_hold_time_bars | 28.2717 |
| exposure | 0.4446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
