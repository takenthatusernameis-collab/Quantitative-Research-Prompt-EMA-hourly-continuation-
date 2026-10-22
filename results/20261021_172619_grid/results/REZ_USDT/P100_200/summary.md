# EMA Hourly Continuation — REZ/USDT P100_200

**Symbol:** REZ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7795 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9588 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -1.3320 |
| sortino_ratio | -0.3136 |
| max_drawdown | 0.3430 |
| cagr | -0.1353 |
| net_avg_win | 81.4881 |
| net_avg_loss | -99.9665 |
| avg_hold_time_bars | 13.3097 |
| exposure | 0.1646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
