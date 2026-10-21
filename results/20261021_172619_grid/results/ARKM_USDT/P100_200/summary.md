# EMA Hourly Continuation — ARKM/USDT P100_200

**Symbol:** ARKM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7051 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8574 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -1.6768 |
| sortino_ratio | -0.3927 |
| max_drawdown | 0.3760 |
| cagr | -0.1652 |
| net_avg_win | 68.6130 |
| net_avg_loss | -85.8274 |
| avg_hold_time_bars | 12.7601 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
