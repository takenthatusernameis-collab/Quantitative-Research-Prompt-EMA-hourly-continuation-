# EMA Hourly Continuation — XEC/USDT P8_144

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9316 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -3.7774 |
| sortino_ratio | -1.2840 |
| max_drawdown | 0.7989 |
| cagr | -0.4592 |
| net_avg_win | 47.0803 |
| net_avg_loss | -67.7033 |
| avg_hold_time_bars | 27.2321 |
| exposure | 0.7221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
