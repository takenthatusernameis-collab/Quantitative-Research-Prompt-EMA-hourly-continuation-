# EMA Hourly Continuation — XRP/USDT P12_26

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.6820 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0491 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -2.1669 |
| sortino_ratio | -0.5931 |
| max_drawdown | 0.5017 |
| cagr | -0.2365 |
| net_avg_win | 56.7513 |
| net_avg_loss | -88.9487 |
| avg_hold_time_bars | 5.4917 |
| exposure | 0.0899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
