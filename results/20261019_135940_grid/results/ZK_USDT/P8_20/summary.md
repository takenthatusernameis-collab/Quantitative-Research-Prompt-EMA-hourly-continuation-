# EMA Hourly Continuation — ZK/USDT P8_20

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1621 |
| net_profit_factor | 0.4898 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -11.0556 |
| sortino_ratio | -6.4714 |
| max_drawdown | 0.9995 |
| cagr | -0.9597 |
| net_avg_win | 13.7282 |
| net_avg_loss | -21.2479 |
| avg_hold_time_bars | 2.8236 |
| exposure | 0.2231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
