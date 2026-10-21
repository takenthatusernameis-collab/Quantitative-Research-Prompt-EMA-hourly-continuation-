# EMA Hourly Continuation — STX/USDT P12_34

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.7284 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.4324 |
| sortino_ratio | -0.8514 |
| max_drawdown | 0.6531 |
| cagr | -0.3222 |
| net_avg_win | 56.6248 |
| net_avg_loss | -75.9471 |
| avg_hold_time_bars | 6.9032 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
