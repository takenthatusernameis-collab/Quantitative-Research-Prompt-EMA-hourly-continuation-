# EMA Hourly Continuation — HTX/USDT P50_55

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.0516 |
| net_win_rate | 0.1380 |
| gross_profit_factor | 0.2965 |
| gross_win_rate | 0.2720 |
| sharpe_ratio | -20.9547 |
| sortino_ratio | -11.3064 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 4.0291 |
| net_avg_loss | -12.5076 |
| avg_hold_time_bars | 2.4673 |
| exposure | 0.1092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
