# EMA Hourly Continuation — AZERO/USDT P20_21

**Symbol:** AZERO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.1508 |
| net_win_rate | 0.2876 |
| gross_profit_factor | 0.7591 |
| gross_win_rate | 0.3594 |
| sharpe_ratio | -16.3133 |
| sortino_ratio | -8.0020 |
| max_drawdown | 1.0000 |
| cagr | -0.9891 |
| net_avg_win | 5.6905 |
| net_avg_loss | -15.2333 |
| avg_hold_time_bars | 2.3991 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
