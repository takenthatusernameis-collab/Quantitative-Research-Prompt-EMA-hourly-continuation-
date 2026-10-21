# EMA Hourly Continuation — XDC/USDT P20_100

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7233 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0469 |
| gross_win_rate | 0.5181 |
| sharpe_ratio | -1.9855 |
| sortino_ratio | -0.6369 |
| max_drawdown | 0.5263 |
| cagr | -0.2521 |
| net_avg_win | 52.6742 |
| net_avg_loss | -77.6608 |
| avg_hold_time_bars | 15.0884 |
| exposure | 0.3415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
