# EMA Hourly Continuation — DIA/USDT P26_100

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -2.5784 |
| sortino_ratio | -0.7937 |
| max_drawdown | 0.6358 |
| cagr | -0.3064 |
| net_avg_win | 61.6930 |
| net_avg_loss | -77.8401 |
| avg_hold_time_bars | 16.6851 |
| exposure | 0.3549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
