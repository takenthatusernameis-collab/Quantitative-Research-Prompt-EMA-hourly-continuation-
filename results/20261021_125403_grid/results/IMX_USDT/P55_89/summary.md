# EMA Hourly Continuation — IMX/USDT P55_89

**Symbol:** IMX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.8151 |
| net_win_rate | 0.5221 |
| gross_profit_factor | 1.0822 |
| gross_win_rate | 0.5221 |
| sharpe_ratio | -1.1319 |
| sortino_ratio | -0.2998 |
| max_drawdown | 0.3180 |
| cagr | -0.1294 |
| net_avg_win | 73.4716 |
| net_avg_loss | -98.4792 |
| avg_hold_time_bars | 5.5074 |
| exposure | 0.0845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
