# EMA Hourly Continuation — AAVE/USDT P34_200

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.9156 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.0960 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -0.4618 |
| sortino_ratio | -0.1157 |
| max_drawdown | 0.2736 |
| cagr | -0.0550 |
| net_avg_win | 90.3718 |
| net_avg_loss | -108.9875 |
| avg_hold_time_bars | 33.0363 |
| exposure | 0.4550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
