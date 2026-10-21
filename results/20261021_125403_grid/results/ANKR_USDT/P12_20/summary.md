# EMA Hourly Continuation — ANKR/USDT P12_20

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6296 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -3.5417 |
| sortino_ratio | -1.0980 |
| max_drawdown | 0.7298 |
| cagr | -0.3945 |
| net_avg_win | 53.8698 |
| net_avg_loss | -81.2517 |
| avg_hold_time_bars | 5.3362 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
