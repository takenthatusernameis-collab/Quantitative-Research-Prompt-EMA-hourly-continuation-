# EMA Hourly Continuation — ENS/USDT P50_55

**Symbol:** ENS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5361 |
| gross_profit_factor | 1.1520 |
| gross_win_rate | 0.5361 |
| sharpe_ratio | -0.6201 |
| sortino_ratio | -0.0884 |
| max_drawdown | 0.1502 |
| cagr | -0.0398 |
| net_avg_win | 81.9190 |
| net_avg_loss | -116.2191 |
| avg_hold_time_bars | 5.0515 |
| exposure | 0.0223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
