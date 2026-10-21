# EMA Hourly Continuation — ENJ/USDT P55_200

**Symbol:** ENJ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8313 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0003 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -0.8911 |
| sortino_ratio | -0.2093 |
| max_drawdown | 0.2878 |
| cagr | -0.0934 |
| net_avg_win | 79.4331 |
| net_avg_loss | -96.9766 |
| avg_hold_time_bars | 34.0407 |
| exposure | 0.4159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
