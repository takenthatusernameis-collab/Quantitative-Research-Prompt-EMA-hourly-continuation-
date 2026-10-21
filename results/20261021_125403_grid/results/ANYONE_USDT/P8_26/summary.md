# EMA Hourly Continuation — ANYONE/USDT P8_26

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.7874 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.0262 |
| sortino_ratio | -0.7653 |
| max_drawdown | 0.5923 |
| cagr | -0.2987 |
| net_avg_win | 65.8809 |
| net_avg_loss | -81.3072 |
| avg_hold_time_bars | 7.7027 |
| exposure | 0.2448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
