# EMA Hourly Continuation — RLC/USDT P12_50

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.7571 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9879 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -2.3998 |
| sortino_ratio | -0.8715 |
| max_drawdown | 0.6543 |
| cagr | -0.3307 |
| net_avg_win | 62.0595 |
| net_avg_loss | -80.4578 |
| avg_hold_time_bars | 12.1196 |
| exposure | 0.3548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
