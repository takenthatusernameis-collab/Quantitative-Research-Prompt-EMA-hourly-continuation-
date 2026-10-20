# EMA Hourly Continuation — AMP/USDT P21_144

**Symbol:** AMP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 819 |
| net_profit_factor | 0.3805 |
| net_win_rate | 0.3919 |
| gross_profit_factor | 0.6419 |
| gross_win_rate | 0.4029 |
| sharpe_ratio | -7.9553 |
| sortino_ratio | -3.1967 |
| max_drawdown | 0.9816 |
| cagr | -0.7934 |
| net_avg_win | 18.7724 |
| net_avg_loss | -31.7978 |
| avg_hold_time_bars | 14.0085 |
| exposure | 0.5215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
