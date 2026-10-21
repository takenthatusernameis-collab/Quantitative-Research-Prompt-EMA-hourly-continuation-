# EMA Hourly Continuation — SNX/USDT P50_144

**Symbol:** SNX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8503 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0617 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -0.9517 |
| sortino_ratio | -0.2498 |
| max_drawdown | 0.3073 |
| cagr | -0.1104 |
| net_avg_win | 84.3984 |
| net_avg_loss | -104.7382 |
| avg_hold_time_bars | 18.5164 |
| exposure | 0.2807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
