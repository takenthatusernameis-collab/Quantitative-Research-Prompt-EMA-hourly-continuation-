# EMA Hourly Continuation — JASMY/USDT P34_89

**Symbol:** JASMY/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.5931 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -4.3868 |
| sortino_ratio | -1.6380 |
| max_drawdown | 0.8746 |
| cagr | -0.5485 |
| net_avg_win | 36.7246 |
| net_avg_loss | -57.7156 |
| avg_hold_time_bars | 6.7778 |
| exposure | 0.2190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
