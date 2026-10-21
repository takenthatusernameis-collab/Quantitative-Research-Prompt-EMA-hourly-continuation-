# EMA Hourly Continuation — RSR/USDT P20_144

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.8631 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0030 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -0.9158 |
| sortino_ratio | -0.2586 |
| max_drawdown | 0.3497 |
| cagr | -0.1149 |
| net_avg_win | 85.3444 |
| net_avg_loss | -99.3947 |
| avg_hold_time_bars | 30.1054 |
| exposure | 0.5323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
