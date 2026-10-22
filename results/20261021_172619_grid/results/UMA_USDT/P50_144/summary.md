# EMA Hourly Continuation — UMA/USDT P50_144

**Symbol:** UMA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7647 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.5762 |
| sortino_ratio | -0.4365 |
| max_drawdown | 0.4161 |
| cagr | -0.1814 |
| net_avg_win | 68.3033 |
| net_avg_loss | -90.2793 |
| avg_hold_time_bars | 16.1578 |
| exposure | 0.2747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
