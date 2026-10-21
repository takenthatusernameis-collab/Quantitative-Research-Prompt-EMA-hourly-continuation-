# EMA Hourly Continuation — BSV/USDT P12_50

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9197 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.3179 |
| sortino_ratio | -1.2250 |
| max_drawdown | 0.7599 |
| cagr | -0.4296 |
| net_avg_win | 48.1969 |
| net_avg_loss | -65.7098 |
| avg_hold_time_bars | 10.0913 |
| exposure | 0.3064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
