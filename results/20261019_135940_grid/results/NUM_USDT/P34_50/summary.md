# EMA Hourly Continuation — NUM/USDT P34_50

**Symbol:** NUM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.2587 |
| net_win_rate | 0.3163 |
| gross_profit_factor | 0.6158 |
| gross_win_rate | 0.3452 |
| sharpe_ratio | -12.2545 |
| sortino_ratio | -5.2896 |
| max_drawdown | 0.9989 |
| cagr | -0.9324 |
| net_avg_win | 12.2296 |
| net_avg_loss | -21.8733 |
| avg_hold_time_bars | 4.0733 |
| exposure | 0.1668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
