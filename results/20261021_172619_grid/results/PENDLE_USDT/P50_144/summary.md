# EMA Hourly Continuation — PENDLE/USDT P50_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7629 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -1.4566 |
| sortino_ratio | -0.3957 |
| max_drawdown | 0.4227 |
| cagr | -0.1674 |
| net_avg_win | 67.3922 |
| net_avg_loss | -83.5918 |
| avg_hold_time_bars | 17.3232 |
| exposure | 0.2850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
