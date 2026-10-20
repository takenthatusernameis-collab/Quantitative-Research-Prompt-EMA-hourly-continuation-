# EMA Hourly Continuation — ORCA/USDT P34_200

**Symbol:** ORCA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7046 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -2.0518 |
| sortino_ratio | -0.5538 |
| max_drawdown | 0.5173 |
| cagr | -0.2299 |
| net_avg_win | 63.7475 |
| net_avg_loss | -88.5082 |
| avg_hold_time_bars | 30.4313 |
| exposure | 0.5035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
