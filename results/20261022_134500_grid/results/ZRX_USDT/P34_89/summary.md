# EMA Hourly Continuation — ZRX/USDT P34_89

**Symbol:** ZRX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.5296 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8689 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -5.3706 |
| sortino_ratio | -1.9451 |
| max_drawdown | 0.9109 |
| cagr | -0.6126 |
| net_avg_win | 33.8404 |
| net_avg_loss | -52.5762 |
| avg_hold_time_bars | 8.9148 |
| exposure | 0.2711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
