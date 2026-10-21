# EMA Hourly Continuation — BCH/USDT P8_200

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.8501 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0447 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -0.8112 |
| sortino_ratio | -0.1780 |
| max_drawdown | 0.3122 |
| cagr | -0.0799 |
| net_avg_win | 89.8955 |
| net_avg_loss | -109.4258 |
| avg_hold_time_bars | 76.0812 |
| exposure | 0.8092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
