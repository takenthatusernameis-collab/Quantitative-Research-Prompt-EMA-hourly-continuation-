# EMA Hourly Continuation — WIF/USDT P100_200

**Symbol:** WIF/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.7476 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9034 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -1.3116 |
| sortino_ratio | -0.2848 |
| max_drawdown | 0.3258 |
| cagr | -0.1227 |
| net_avg_win | 74.7644 |
| net_avg_loss | -91.7429 |
| avg_hold_time_bars | 12.4483 |
| exposure | 0.1313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
