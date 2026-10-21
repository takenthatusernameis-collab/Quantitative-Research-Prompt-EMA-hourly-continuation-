# EMA Hourly Continuation — BONK/USDT P34_144

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.9009 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -0.5161 |
| sortino_ratio | -0.1354 |
| max_drawdown | 0.2699 |
| cagr | -0.0640 |
| net_avg_win | 80.9391 |
| net_avg_loss | -95.9803 |
| avg_hold_time_bars | 24.8138 |
| exposure | 0.3756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
