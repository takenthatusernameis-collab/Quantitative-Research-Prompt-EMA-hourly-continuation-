# EMA Hourly Continuation — POPCAT/USDT P89_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.7857 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9703 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -1.3122 |
| sortino_ratio | -0.3269 |
| max_drawdown | 0.2983 |
| cagr | -0.1405 |
| net_avg_win | 79.2842 |
| net_avg_loss | -98.6149 |
| avg_hold_time_bars | 7.7126 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
