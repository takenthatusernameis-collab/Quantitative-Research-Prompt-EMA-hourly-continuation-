# EMA Hourly Continuation — OP/USDT P21_34

**Symbol:** OP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1134 |
| net_profit_factor | 0.3179 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -10.6107 |
| sortino_ratio | -5.0908 |
| max_drawdown | 0.9984 |
| cagr | -0.9228 |
| net_avg_win | 9.8385 |
| net_avg_loss | -22.1445 |
| avg_hold_time_bars | 2.3183 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
