# EMA Hourly Continuation — MEW/USDT P8_200

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.9308 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0486 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -0.2790 |
| sortino_ratio | -0.0604 |
| max_drawdown | 0.2041 |
| cagr | -0.0306 |
| net_avg_win | 85.6454 |
| net_avg_loss | -98.7075 |
| avg_hold_time_bars | 79.5482 |
| exposure | 0.8244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
