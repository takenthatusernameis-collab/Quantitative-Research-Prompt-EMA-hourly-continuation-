# EMA Hourly Continuation — FLOW/USDT P12_20

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1554 |
| net_profit_factor | 0.2448 |
| net_win_rate | 0.3745 |
| gross_profit_factor | 0.7450 |
| gross_win_rate | 0.4170 |
| sharpe_ratio | -15.3828 |
| sortino_ratio | -8.7482 |
| max_drawdown | 1.0000 |
| cagr | -0.9891 |
| net_avg_win | 5.5683 |
| net_avg_loss | -13.6221 |
| avg_hold_time_bars | 2.2452 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
