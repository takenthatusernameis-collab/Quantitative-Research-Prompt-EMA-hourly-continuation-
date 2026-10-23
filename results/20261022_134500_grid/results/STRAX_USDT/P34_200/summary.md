# EMA Hourly Continuation — STRAX/USDT P34_200

**Symbol:** STRAX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.5181 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.7560 |
| gross_win_rate | 0.4241 |
| sharpe_ratio | -5.1076 |
| sortino_ratio | -1.6769 |
| max_drawdown | 0.8613 |
| cagr | -0.5467 |
| net_avg_win | 41.1590 |
| net_avg_loss | -56.7417 |
| avg_hold_time_bars | 18.1852 |
| exposure | 0.4490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
