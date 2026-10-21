# EMA Hourly Continuation — SKY/USDT P26_89

**Symbol:** SKY/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7402 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9566 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.0582 |
| sortino_ratio | -0.6314 |
| max_drawdown | 0.5093 |
| cagr | -0.2517 |
| net_avg_win | 69.3186 |
| net_avg_loss | -89.7432 |
| avg_hold_time_bars | 17.1383 |
| exposure | 0.3593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
