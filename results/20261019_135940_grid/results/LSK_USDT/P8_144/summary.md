# EMA Hourly Continuation — LSK/USDT P8_144

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 1.0155 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.8743 |
| sortino_ratio | -0.8649 |
| max_drawdown | 0.6867 |
| cagr | -0.3475 |
| net_avg_win | 63.7082 |
| net_avg_loss | -86.0572 |
| avg_hold_time_bars | 34.8504 |
| exposure | 0.7414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
