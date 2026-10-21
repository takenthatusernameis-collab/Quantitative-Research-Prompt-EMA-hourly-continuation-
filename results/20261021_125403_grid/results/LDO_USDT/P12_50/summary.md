# EMA Hourly Continuation — LDO/USDT P12_50

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.7251 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9012 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -2.4115 |
| sortino_ratio | -0.8647 |
| max_drawdown | 0.6450 |
| cagr | -0.3280 |
| net_avg_win | 54.9735 |
| net_avg_loss | -69.8225 |
| avg_hold_time_bars | 10.4241 |
| exposure | 0.2995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
