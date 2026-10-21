# EMA Hourly Continuation — IOST/USDT P20_144

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.9333 |
| net_win_rate | 0.5439 |
| gross_profit_factor | 1.1853 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | -0.4132 |
| sortino_ratio | -0.1210 |
| max_drawdown | 0.3269 |
| cagr | -0.0595 |
| net_avg_win | 89.5302 |
| net_avg_loss | -114.4017 |
| avg_hold_time_bars | 28.1902 |
| exposure | 0.5254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
