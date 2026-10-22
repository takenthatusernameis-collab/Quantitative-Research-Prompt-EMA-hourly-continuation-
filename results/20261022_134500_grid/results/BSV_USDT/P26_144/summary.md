# EMA Hourly Continuation — BSV/USDT P26_144

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.4871 |
| net_win_rate | 0.4208 |
| gross_profit_factor | 0.8014 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -5.6293 |
| sortino_ratio | -1.8948 |
| max_drawdown | 0.9072 |
| cagr | -0.6088 |
| net_avg_win | 34.8103 |
| net_avg_loss | -51.9153 |
| avg_hold_time_bars | 17.4003 |
| exposure | 0.4643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
