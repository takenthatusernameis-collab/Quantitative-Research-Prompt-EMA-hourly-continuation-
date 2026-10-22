# EMA Hourly Continuation — BTC/USDT P8_100

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4309 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -6.2326 |
| sortino_ratio | -2.0894 |
| max_drawdown | 0.9571 |
| cagr | -0.6662 |
| net_avg_win | 24.1334 |
| net_avg_loss | -45.4143 |
| avg_hold_time_bars | 25.6090 |
| exposure | 0.6863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
