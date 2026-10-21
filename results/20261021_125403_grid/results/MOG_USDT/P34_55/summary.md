# EMA Hourly Continuation — MOG/USDT P34_55

**Symbol:** MOG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.8962 |
| net_win_rate | 0.5314 |
| gross_profit_factor | 1.1386 |
| gross_win_rate | 0.5314 |
| sharpe_ratio | -0.6415 |
| sortino_ratio | -0.1594 |
| max_drawdown | 0.2948 |
| cagr | -0.0733 |
| net_avg_win | 96.1164 |
| net_avg_loss | -121.6044 |
| avg_hold_time_bars | 6.0627 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
