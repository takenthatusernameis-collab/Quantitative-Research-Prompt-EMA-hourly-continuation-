# EMA Hourly Continuation — LISTA/USDT P12_89

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.6851 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9512 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -3.2355 |
| sortino_ratio | -1.1846 |
| max_drawdown | 0.7362 |
| cagr | -0.4344 |
| net_avg_win | 52.6306 |
| net_avg_loss | -70.7742 |
| avg_hold_time_bars | 17.3675 |
| exposure | 0.5384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
