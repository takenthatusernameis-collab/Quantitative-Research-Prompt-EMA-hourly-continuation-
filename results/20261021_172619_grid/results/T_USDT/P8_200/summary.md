# EMA Hourly Continuation — T/USDT P8_200

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.9281 |
| net_win_rate | 0.5426 |
| gross_profit_factor | 1.1639 |
| gross_win_rate | 0.5426 |
| sharpe_ratio | -0.3153 |
| sortino_ratio | -0.0727 |
| max_drawdown | 0.2260 |
| cagr | -0.0365 |
| net_avg_win | 82.4453 |
| net_avg_loss | -105.3998 |
| avg_hold_time_bars | 68.8101 |
| exposure | 0.8034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
