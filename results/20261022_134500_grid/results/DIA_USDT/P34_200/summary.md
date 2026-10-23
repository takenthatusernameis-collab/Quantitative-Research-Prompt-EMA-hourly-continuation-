# EMA Hourly Continuation — DIA/USDT P34_200

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6942 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9986 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -2.1408 |
| sortino_ratio | -0.6237 |
| max_drawdown | 0.5847 |
| cagr | -0.2560 |
| net_avg_win | 56.0417 |
| net_avg_loss | -80.7227 |
| avg_hold_time_bars | 24.6268 |
| exposure | 0.4747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
