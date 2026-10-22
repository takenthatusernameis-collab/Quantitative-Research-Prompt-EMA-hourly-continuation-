# EMA Hourly Continuation — VR/USDT P34_55

**Symbol:** VR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.5210 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.7535 |
| gross_win_rate | 0.4170 |
| sharpe_ratio | -3.4434 |
| sortino_ratio | -0.7481 |
| max_drawdown | 0.5907 |
| cagr | -0.2968 |
| net_avg_win | 65.8306 |
| net_avg_loss | -88.8098 |
| avg_hold_time_bars | 7.7234 |
| exposure | 0.0825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
