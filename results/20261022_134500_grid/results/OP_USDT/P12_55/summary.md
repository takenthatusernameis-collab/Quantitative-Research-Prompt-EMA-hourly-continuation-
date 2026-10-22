# EMA Hourly Continuation — OP/USDT P12_55

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.5672 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -5.7552 |
| sortino_ratio | -2.5066 |
| max_drawdown | 0.9580 |
| cagr | -0.7041 |
| net_avg_win | 27.6355 |
| net_avg_loss | -42.6769 |
| avg_hold_time_bars | 9.1250 |
| exposure | 0.4015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
