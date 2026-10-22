# EMA Hourly Continuation — EUL/USDT P20_200

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8073 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -1.1167 |
| sortino_ratio | -0.2794 |
| max_drawdown | 0.2984 |
| cagr | -0.1219 |
| net_avg_win | 77.7574 |
| net_avg_loss | -91.4455 |
| avg_hold_time_bars | 40.5649 |
| exposure | 0.5679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
