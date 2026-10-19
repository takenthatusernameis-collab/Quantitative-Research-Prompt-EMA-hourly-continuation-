# EMA Hourly Continuation — JASMY/USDT P50_89

**Symbol:** JASMY/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.5622 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -4.9191 |
| sortino_ratio | -1.8212 |
| max_drawdown | 0.8955 |
| cagr | -0.5852 |
| net_avg_win | 34.6464 |
| net_avg_loss | -56.6464 |
| avg_hold_time_bars | 4.5269 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
