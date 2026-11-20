# EMA Hourly Continuation — P2P/USDT P8_21

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1596 |
| net_profit_factor | 0.2982 |
| net_win_rate | 0.3064 |
| gross_profit_factor | 0.5110 |
| gross_win_rate | 0.3083 |
| sharpe_ratio | -15.2868 |
| sortino_ratio | -8.5974 |
| max_drawdown | 1.0000 |
| cagr | -0.9869 |
| net_avg_win | 8.6883 |
| net_avg_loss | -12.8712 |
| avg_hold_time_bars | 3.6197 |
| exposure | 0.2626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
