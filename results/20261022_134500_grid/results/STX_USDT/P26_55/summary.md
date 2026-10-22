# EMA Hourly Continuation — STX/USDT P26_55

**Symbol:** STX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 868 |
| net_profit_factor | 0.4874 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8476 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -6.7018 |
| sortino_ratio | -2.7713 |
| max_drawdown | 0.9698 |
| cagr | -0.7434 |
| net_avg_win | 23.2325 |
| net_avg_loss | -39.9926 |
| avg_hold_time_bars | 4.5207 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
