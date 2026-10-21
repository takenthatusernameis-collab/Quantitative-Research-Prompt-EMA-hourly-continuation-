# EMA Hourly Continuation — SSV/USDT P12_20

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6707 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -2.9641 |
| sortino_ratio | -0.8480 |
| max_drawdown | 0.6397 |
| cagr | -0.3226 |
| net_avg_win | 68.5008 |
| net_avg_loss | -87.5476 |
| avg_hold_time_bars | 4.8015 |
| exposure | 0.0876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
