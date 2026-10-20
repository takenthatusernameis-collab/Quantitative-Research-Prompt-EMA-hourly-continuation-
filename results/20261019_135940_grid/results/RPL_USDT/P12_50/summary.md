# EMA Hourly Continuation — RPL/USDT P12_50

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.6045 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -5.3335 |
| sortino_ratio | -2.2517 |
| max_drawdown | 0.9386 |
| cagr | -0.6648 |
| net_avg_win | 33.7611 |
| net_avg_loss | -48.4252 |
| avg_hold_time_bars | 9.6024 |
| exposure | 0.3968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
