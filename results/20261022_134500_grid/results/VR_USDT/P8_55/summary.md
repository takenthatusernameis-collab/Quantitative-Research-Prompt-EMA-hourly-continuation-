# EMA Hourly Continuation — VR/USDT P8_55

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.5160 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.7810 |
| gross_win_rate | 0.4164 |
| sharpe_ratio | -9.6340 |
| sortino_ratio | -4.3100 |
| max_drawdown | 0.9975 |
| cagr | -0.9087 |
| net_avg_win | 24.5635 |
| net_avg_loss | -32.3064 |
| avg_hold_time_bars | 10.0261 |
| exposure | 0.4881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
