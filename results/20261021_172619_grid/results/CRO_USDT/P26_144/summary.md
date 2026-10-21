# EMA Hourly Continuation — CRO/USDT P26_144

**Symbol:** CRO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7327 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6679 |
| sortino_ratio | -0.4365 |
| max_drawdown | 0.4315 |
| cagr | -0.1817 |
| net_avg_win | 64.9105 |
| net_avg_loss | -88.5966 |
| avg_hold_time_bars | 32.3293 |
| exposure | 0.4908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
