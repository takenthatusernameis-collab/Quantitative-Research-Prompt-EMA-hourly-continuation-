# EMA Hourly Continuation — AXS/USDT P20_89

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0626 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -3.2659 |
| sortino_ratio | -1.1804 |
| max_drawdown | 0.7703 |
| cagr | -0.4305 |
| net_avg_win | 49.6711 |
| net_avg_loss | -72.6521 |
| avg_hold_time_bars | 12.6924 |
| exposure | 0.3791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
