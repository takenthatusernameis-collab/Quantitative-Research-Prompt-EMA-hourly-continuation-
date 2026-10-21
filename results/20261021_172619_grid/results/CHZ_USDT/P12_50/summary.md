# EMA Hourly Continuation — CHZ/USDT P12_50

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.7766 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0142 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -2.0627 |
| sortino_ratio | -0.7565 |
| max_drawdown | 0.6009 |
| cagr | -0.2946 |
| net_avg_win | 61.6794 |
| net_avg_loss | -80.3990 |
| avg_hold_time_bars | 10.7156 |
| exposure | 0.3185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
