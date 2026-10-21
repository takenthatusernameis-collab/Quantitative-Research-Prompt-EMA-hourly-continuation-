# EMA Hourly Continuation — ARB/USDT P12_34

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7615 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0212 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -1.8292 |
| sortino_ratio | -0.5991 |
| max_drawdown | 0.5362 |
| cagr | -0.2401 |
| net_avg_win | 60.2537 |
| net_avg_loss | -81.9140 |
| avg_hold_time_bars | 7.0674 |
| exposure | 0.1667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
