# EMA Hourly Continuation — LDO/USDT P8_55

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.7742 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9376 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -2.0184 |
| sortino_ratio | -0.7071 |
| max_drawdown | 0.5673 |
| cagr | -0.2784 |
| net_avg_win | 65.6718 |
| net_avg_loss | -79.6438 |
| avg_hold_time_bars | 18.0398 |
| exposure | 0.4945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
