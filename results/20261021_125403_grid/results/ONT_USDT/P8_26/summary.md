# EMA Hourly Continuation — ONT/USDT P8_26

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.6998 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 0.9844 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -3.0190 |
| sortino_ratio | -1.1519 |
| max_drawdown | 0.7485 |
| cagr | -0.4095 |
| net_avg_win | 48.5659 |
| net_avg_loss | -68.4261 |
| avg_hold_time_bars | 6.6835 |
| exposure | 0.2150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
