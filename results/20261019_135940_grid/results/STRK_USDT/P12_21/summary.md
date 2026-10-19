# EMA Hourly Continuation — STRK/USDT P12_21

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1430 |
| net_profit_factor | 0.2902 |
| net_win_rate | 0.3972 |
| gross_profit_factor | 0.6879 |
| gross_win_rate | 0.4210 |
| sharpe_ratio | -12.5805 |
| sortino_ratio | -6.7581 |
| max_drawdown | 0.9998 |
| cagr | -0.9681 |
| net_avg_win | 7.1961 |
| net_avg_loss | -16.3406 |
| avg_hold_time_bars | 2.1741 |
| exposure | 0.1413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
