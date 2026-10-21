# EMA Hourly Continuation — AMP/USDT P8_50

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.5248 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.6994 |
| gross_win_rate | 0.4132 |
| sharpe_ratio | -5.6893 |
| sortino_ratio | -2.2403 |
| max_drawdown | 0.9301 |
| cagr | -0.6456 |
| net_avg_win | 32.0649 |
| net_avg_loss | -43.0235 |
| avg_hold_time_bars | 10.8161 |
| exposure | 0.3795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
