# EMA Hourly Continuation — EDU/USDT P100_200

**Symbol:** EDU/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7053 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -1.8673 |
| sortino_ratio | -0.4650 |
| max_drawdown | 0.4337 |
| cagr | -0.1930 |
| net_avg_win | 68.9709 |
| net_avg_loss | -87.5278 |
| avg_hold_time_bars | 11.2052 |
| exposure | 0.1557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
