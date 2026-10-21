# EMA Hourly Continuation — STRAX/USDT P55_200

**Symbol:** STRAX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5454 |
| net_win_rate | 0.4108 |
| gross_profit_factor | 0.7066 |
| gross_win_rate | 0.4108 |
| sharpe_ratio | -3.6675 |
| sortino_ratio | -0.9756 |
| max_drawdown | 0.6780 |
| cagr | -0.3629 |
| net_avg_win | 55.9023 |
| net_avg_loss | -71.4508 |
| avg_hold_time_bars | 20.7592 |
| exposure | 0.3350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
