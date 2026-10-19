# EMA Hourly Continuation — BTT/USDT P8_200

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.5130 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8476 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.7203 |
| sortino_ratio | -0.9119 |
| max_drawdown | 0.6945 |
| cagr | -0.3624 |
| net_avg_win | 51.3129 |
| net_avg_loss | -82.2635 |
| avg_hold_time_bars | 59.3214 |
| exposure | 0.8305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
