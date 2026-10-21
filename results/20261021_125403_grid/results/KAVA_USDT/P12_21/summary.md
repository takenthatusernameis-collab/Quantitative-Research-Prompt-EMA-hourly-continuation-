# EMA Hourly Continuation — KAVA/USDT P12_21

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.5620 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -4.5259 |
| sortino_ratio | -1.3880 |
| max_drawdown | 0.8072 |
| cagr | -0.4766 |
| net_avg_win | 49.5505 |
| net_avg_loss | -73.9482 |
| avg_hold_time_bars | 5.8070 |
| exposure | 0.1204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
