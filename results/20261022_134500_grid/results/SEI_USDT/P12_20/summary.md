# EMA Hourly Continuation — SEI/USDT P12_20

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1448 |
| net_profit_factor | 0.4099 |
| net_win_rate | 0.4164 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -12.2652 |
| sortino_ratio | -6.6188 |
| max_drawdown | 0.9998 |
| cagr | -0.9668 |
| net_avg_win | 11.5190 |
| net_avg_loss | -20.0521 |
| avg_hold_time_bars | 2.1913 |
| exposure | 0.1442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
