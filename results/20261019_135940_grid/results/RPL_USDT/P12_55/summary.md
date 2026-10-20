# EMA Hourly Continuation — RPL/USDT P12_55

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.5976 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.9640 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -5.1988 |
| sortino_ratio | -2.1588 |
| max_drawdown | 0.9306 |
| cagr | -0.6485 |
| net_avg_win | 34.1246 |
| net_avg_loss | -48.0636 |
| avg_hold_time_bars | 10.5984 |
| exposure | 0.4240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
