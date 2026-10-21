# EMA Hourly Continuation — RAY/USDT P8_144

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8466 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 0.9854 |
| gross_win_rate | 0.4975 |
| sharpe_ratio | -1.0149 |
| sortino_ratio | -0.2915 |
| max_drawdown | 0.3644 |
| cagr | -0.1284 |
| net_avg_win | 80.1408 |
| net_avg_loss | -93.7282 |
| avg_hold_time_bars | 38.6634 |
| exposure | 0.7100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
