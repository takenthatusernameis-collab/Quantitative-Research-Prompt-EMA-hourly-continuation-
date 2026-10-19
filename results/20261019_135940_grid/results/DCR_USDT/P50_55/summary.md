# EMA Hourly Continuation — DCR/USDT P50_55

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 847 |
| net_profit_factor | 0.2436 |
| net_win_rate | 0.3459 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4227 |
| sharpe_ratio | -12.4778 |
| sortino_ratio | -5.3238 |
| max_drawdown | 0.9993 |
| cagr | -0.9426 |
| net_avg_win | 10.9829 |
| net_avg_loss | -23.8458 |
| avg_hold_time_bars | 2.5809 |
| exposure | 0.0989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
