# EMA Hourly Continuation — 1INCH/USDT P12_55

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7065 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9502 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.9826 |
| sortino_ratio | -1.0865 |
| max_drawdown | 0.7241 |
| cagr | -0.3918 |
| net_avg_win | 54.5045 |
| net_avg_loss | -72.7554 |
| avg_hold_time_bars | 12.8213 |
| exposure | 0.3782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
