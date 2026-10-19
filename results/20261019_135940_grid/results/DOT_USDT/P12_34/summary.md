# EMA Hourly Continuation — DOT/USDT P12_34

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1277 |
| net_profit_factor | 0.4330 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.9332 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -9.6953 |
| sortino_ratio | -4.8723 |
| max_drawdown | 0.9980 |
| cagr | -0.9139 |
| net_avg_win | 13.5118 |
| net_avg_loss | -24.6837 |
| avg_hold_time_bars | 4.1464 |
| exposure | 0.2407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
