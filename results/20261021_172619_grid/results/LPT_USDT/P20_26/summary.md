# EMA Hourly Continuation — LPT/USDT P20_26

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.6095 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9295 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -2.8980 |
| sortino_ratio | -0.7032 |
| max_drawdown | 0.5680 |
| cagr | -0.2783 |
| net_avg_win | 63.7052 |
| net_avg_loss | -95.4638 |
| avg_hold_time_bars | 4.1394 |
| exposure | 0.0540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
