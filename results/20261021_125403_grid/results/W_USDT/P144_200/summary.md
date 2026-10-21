# EMA Hourly Continuation — W/USDT P144_200

**Symbol:** W/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 1.0120 |
| net_win_rate | 0.5676 |
| gross_profit_factor | 1.2961 |
| gross_win_rate | 0.5676 |
| sharpe_ratio | 0.0958 |
| sortino_ratio | 0.0190 |
| max_drawdown | 0.1609 |
| cagr | 0.0045 |
| net_avg_win | 92.1329 |
| net_avg_loss | -119.4928 |
| avg_hold_time_bars | 7.2324 |
| exposure | 0.0608 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
