# EMA Hourly Continuation — YGG/USDT P50_55

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.3039 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -10.7043 |
| sortino_ratio | -4.4831 |
| max_drawdown | 0.9975 |
| cagr | -0.9070 |
| net_avg_win | 12.7324 |
| net_avg_loss | -28.4316 |
| avg_hold_time_bars | 1.9326 |
| exposure | 0.0740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
