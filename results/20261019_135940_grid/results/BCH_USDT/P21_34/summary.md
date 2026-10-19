# EMA Hourly Continuation — BCH/USDT P21_34

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.2196 |
| net_win_rate | 0.3597 |
| gross_profit_factor | 0.6504 |
| gross_win_rate | 0.4092 |
| sharpe_ratio | -13.7924 |
| sortino_ratio | -6.6722 |
| max_drawdown | 0.9999 |
| cagr | -0.9711 |
| net_avg_win | 7.0331 |
| net_avg_loss | -17.9942 |
| avg_hold_time_bars | 2.5531 |
| exposure | 0.1290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
