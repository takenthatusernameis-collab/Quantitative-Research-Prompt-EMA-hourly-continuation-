# EMA Hourly Continuation — ADA/USDT P26_144

**Symbol:** ADA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5544 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8896 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -4.0200 |
| sortino_ratio | -1.2232 |
| max_drawdown | 0.7876 |
| cagr | -0.4530 |
| net_avg_win | 44.3175 |
| net_avg_loss | -68.1229 |
| avg_hold_time_bars | 21.8088 |
| exposure | 0.4719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
