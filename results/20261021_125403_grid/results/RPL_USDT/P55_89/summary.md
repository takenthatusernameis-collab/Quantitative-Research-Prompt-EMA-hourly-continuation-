# EMA Hourly Continuation — RPL/USDT P55_89

**Symbol:** RPL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6864 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -2.5115 |
| sortino_ratio | -0.7244 |
| max_drawdown | 0.5774 |
| cagr | -0.2818 |
| net_avg_win | 63.5391 |
| net_avg_loss | -84.3491 |
| avg_hold_time_bars | 8.1247 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
