# EMA Hourly Continuation — IO/USDT P21_200

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6305 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -3.1585 |
| sortino_ratio | -0.9295 |
| max_drawdown | 0.6646 |
| cagr | -0.3613 |
| net_avg_win | 58.9160 |
| net_avg_loss | -77.8012 |
| avg_hold_time_bars | 30.9111 |
| exposure | 0.6225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
