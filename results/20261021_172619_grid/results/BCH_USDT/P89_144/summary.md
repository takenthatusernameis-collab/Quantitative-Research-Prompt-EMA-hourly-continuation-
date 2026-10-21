# EMA Hourly Continuation — BCH/USDT P89_144

**Symbol:** BCH/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6783 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9680 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.0215 |
| sortino_ratio | -0.4741 |
| max_drawdown | 0.4609 |
| cagr | -0.1948 |
| net_avg_win | 67.5232 |
| net_avg_loss | -95.8932 |
| avg_hold_time_bars | 8.2547 |
| exposure | 0.1002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
