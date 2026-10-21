# EMA Hourly Continuation — WIN/USDT P8_55

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.6789 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9515 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -3.1741 |
| sortino_ratio | -1.1761 |
| max_drawdown | 0.7607 |
| cagr | -0.4167 |
| net_avg_win | 48.2625 |
| net_avg_loss | -66.9652 |
| avg_hold_time_bars | 15.2388 |
| exposure | 0.4641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
