# EMA Hourly Continuation — TAO/USDT P12_21

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.8558 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1118 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.7508 |
| sortino_ratio | -0.1635 |
| max_drawdown | 0.2920 |
| cagr | -0.0736 |
| net_avg_win | 86.3968 |
| net_avg_loss | -112.1701 |
| avg_hold_time_bars | 5.1053 |
| exposure | 0.0529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
