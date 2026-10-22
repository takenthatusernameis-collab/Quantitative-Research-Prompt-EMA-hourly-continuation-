# EMA Hourly Continuation — MANTA/USDT P100_200

**Symbol:** MANTA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8482 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -2.0806 |
| sortino_ratio | -0.4951 |
| max_drawdown | 0.4492 |
| cagr | -0.2037 |
| net_avg_win | 68.1159 |
| net_avg_loss | -87.0418 |
| avg_hold_time_bars | 13.0893 |
| exposure | 0.1666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
