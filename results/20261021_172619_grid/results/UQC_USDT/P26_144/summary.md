# EMA Hourly Continuation — UQC/USDT P26_144

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.4171 |
| net_win_rate | 0.3316 |
| gross_profit_factor | 0.5173 |
| gross_win_rate | 0.3316 |
| sharpe_ratio | -3.9092 |
| sortino_ratio | -0.7606 |
| max_drawdown | 0.5991 |
| cagr | -0.3040 |
| net_avg_win | 65.9643 |
| net_avg_loss | -78.4636 |
| avg_hold_time_bars | 75.1378 |
| exposure | 0.6665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
