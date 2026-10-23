# EMA Hourly Continuation — ENJ/USDT P8_144

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7294 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9689 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -1.9742 |
| sortino_ratio | -0.5683 |
| max_drawdown | 0.5288 |
| cagr | -0.2364 |
| net_avg_win | 64.2505 |
| net_avg_loss | -86.4213 |
| avg_hold_time_bars | 41.5981 |
| exposure | 0.7868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
