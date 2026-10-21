# EMA Hourly Continuation — GRT/USDT P21_144

**Symbol:** GRT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.8185 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9819 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.2978 |
| sortino_ratio | -0.3564 |
| max_drawdown | 0.4035 |
| cagr | -0.1533 |
| net_avg_win | 84.0166 |
| net_avg_loss | -100.4590 |
| avg_hold_time_bars | 29.2312 |
| exposure | 0.4921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
