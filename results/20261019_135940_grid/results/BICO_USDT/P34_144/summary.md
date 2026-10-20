# EMA Hourly Continuation — BICO/USDT P34_144

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.8538 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -2.6541 |
| sortino_ratio | -0.7693 |
| max_drawdown | 0.6134 |
| cagr | -0.3025 |
| net_avg_win | 53.8277 |
| net_avg_loss | -72.7862 |
| avg_hold_time_bars | 24.2067 |
| exposure | 0.4632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
