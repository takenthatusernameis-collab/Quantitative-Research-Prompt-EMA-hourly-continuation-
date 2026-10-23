# EMA Hourly Continuation — DGB/USDT P34_100

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5514 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -6.1356 |
| sortino_ratio | -2.3069 |
| max_drawdown | 0.9456 |
| cagr | -0.6851 |
| net_avg_win | 35.8599 |
| net_avg_loss | -52.2811 |
| avg_hold_time_bars | 8.7469 |
| exposure | 0.2890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
