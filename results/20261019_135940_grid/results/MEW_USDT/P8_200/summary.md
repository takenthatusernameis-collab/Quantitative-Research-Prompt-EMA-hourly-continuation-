# EMA Hourly Continuation — MEW/USDT P8_200

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7822 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0163 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -1.2124 |
| sortino_ratio | -0.2937 |
| max_drawdown | 0.3505 |
| cagr | -0.1313 |
| net_avg_win | 71.3208 |
| net_avg_loss | -94.3203 |
| avg_hold_time_bars | 61.9017 |
| exposure | 0.8300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
