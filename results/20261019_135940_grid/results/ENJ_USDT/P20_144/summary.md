# EMA Hourly Continuation — ENJ/USDT P20_144

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7276 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 1.0483 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -2.2763 |
| sortino_ratio | -0.6971 |
| max_drawdown | 0.6142 |
| cagr | -0.2822 |
| net_avg_win | 64.9571 |
| net_avg_loss | -86.6752 |
| avg_hold_time_bars | 26.6512 |
| exposure | 0.5704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
