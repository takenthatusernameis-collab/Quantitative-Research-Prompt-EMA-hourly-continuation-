# EMA Hourly Continuation — REZ/USDT P34_200

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.8629 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.1139 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -0.9188 |
| sortino_ratio | -0.2584 |
| max_drawdown | 0.3411 |
| cagr | -0.1170 |
| net_avg_win | 83.3892 |
| net_avg_loss | -105.6189 |
| avg_hold_time_bars | 30.4517 |
| exposure | 0.5381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
