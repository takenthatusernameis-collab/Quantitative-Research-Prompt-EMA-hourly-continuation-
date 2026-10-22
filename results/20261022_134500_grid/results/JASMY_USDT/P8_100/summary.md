# EMA Hourly Continuation — JASMY/USDT P8_100

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.7283 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0184 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -2.4232 |
| sortino_ratio | -0.8704 |
| max_drawdown | 0.6763 |
| cagr | -0.3389 |
| net_avg_win | 52.8115 |
| net_avg_loss | -74.7956 |
| avg_hold_time_bars | 22.7492 |
| exposure | 0.6680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
