# EMA Hourly Continuation — FIDA/USDT P12_34

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -3.6865 |
| sortino_ratio | -1.4085 |
| max_drawdown | 0.8048 |
| cagr | -0.4767 |
| net_avg_win | 40.8264 |
| net_avg_loss | -57.4058 |
| avg_hold_time_bars | 7.6219 |
| exposure | 0.2490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
