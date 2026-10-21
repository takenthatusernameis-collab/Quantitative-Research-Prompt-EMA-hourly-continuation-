# EMA Hourly Continuation — TAO/USDT P21_26

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.7240 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -1.1752 |
| sortino_ratio | -0.1758 |
| max_drawdown | 0.3027 |
| cagr | -0.0779 |
| net_avg_win | 92.9963 |
| net_avg_loss | -115.1552 |
| avg_hold_time_bars | 4.6727 |
| exposure | 0.0234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
