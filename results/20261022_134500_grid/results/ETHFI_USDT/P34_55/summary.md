# EMA Hourly Continuation — ETHFI/USDT P34_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.4962 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -6.9749 |
| sortino_ratio | -3.0218 |
| max_drawdown | 0.9743 |
| cagr | -0.7666 |
| net_avg_win | 22.7364 |
| net_avg_loss | -37.8391 |
| avg_hold_time_bars | 3.1200 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
