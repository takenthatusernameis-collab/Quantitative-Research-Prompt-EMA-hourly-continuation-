# EMA Hourly Continuation — ETH/USDT P26_50

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.2424 |
| net_win_rate | 0.3836 |
| gross_profit_factor | 0.8737 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -11.5713 |
| sortino_ratio | -5.0719 |
| max_drawdown | 0.9989 |
| cagr | -0.9318 |
| net_avg_win | 8.9746 |
| net_avg_loss | -23.0475 |
| avg_hold_time_bars | 3.8459 |
| exposure | 0.1622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
