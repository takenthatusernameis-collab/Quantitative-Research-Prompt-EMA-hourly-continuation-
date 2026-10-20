# EMA Hourly Continuation — GLM/USDT P8_21

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1518 |
| net_profit_factor | 0.4041 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -10.8872 |
| sortino_ratio | -5.9986 |
| max_drawdown | 0.9994 |
| cagr | -0.9496 |
| net_avg_win | 10.1600 |
| net_avg_loss | -19.7077 |
| avg_hold_time_bars | 3.7233 |
| exposure | 0.2569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
