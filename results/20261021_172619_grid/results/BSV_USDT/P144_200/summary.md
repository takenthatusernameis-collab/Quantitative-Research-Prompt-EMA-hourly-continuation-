# EMA Hourly Continuation — BSV/USDT P144_200

**Symbol:** BSV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.5220 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.7567 |
| gross_win_rate | 0.4272 |
| sharpe_ratio | -2.9509 |
| sortino_ratio | -0.6046 |
| max_drawdown | 0.5033 |
| cagr | -0.2432 |
| net_avg_win | 62.4417 |
| net_avg_loss | -89.2152 |
| avg_hold_time_bars | 7.7330 |
| exposure | 0.0724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
