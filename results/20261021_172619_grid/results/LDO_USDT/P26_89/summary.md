# EMA Hourly Continuation — LDO/USDT P26_89

**Symbol:** LDO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7311 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -2.1740 |
| sortino_ratio | -0.6753 |
| max_drawdown | 0.5537 |
| cagr | -0.2672 |
| net_avg_win | 65.4639 |
| net_avg_loss | -80.2711 |
| avg_hold_time_bars | 13.7794 |
| exposure | 0.2981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
