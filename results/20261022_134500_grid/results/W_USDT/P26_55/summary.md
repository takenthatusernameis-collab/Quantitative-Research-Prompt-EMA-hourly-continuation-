# EMA Hourly Continuation — W/USDT P26_55

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 906 |
| net_profit_factor | 0.5916 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -5.6762 |
| sortino_ratio | -2.4027 |
| max_drawdown | 0.9497 |
| cagr | -0.6907 |
| net_avg_win | 31.9137 |
| net_avg_loss | -48.7346 |
| avg_hold_time_bars | 4.1413 |
| exposure | 0.1705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
