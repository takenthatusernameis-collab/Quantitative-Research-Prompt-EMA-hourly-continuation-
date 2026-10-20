# EMA Hourly Continuation — EDU/USDT P21_144

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.6999 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.4731 |
| sortino_ratio | -0.7969 |
| max_drawdown | 0.6394 |
| cagr | -0.3159 |
| net_avg_win | 56.5711 |
| net_avg_loss | -75.7620 |
| avg_hold_time_bars | 23.4229 |
| exposure | 0.5565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
