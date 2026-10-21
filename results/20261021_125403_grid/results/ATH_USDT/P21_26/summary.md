# EMA Hourly Continuation — ATH/USDT P21_26

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 137 |
| net_profit_factor | 1.0521 |
| net_win_rate | 0.5912 |
| gross_profit_factor | 1.4278 |
| gross_win_rate | 0.5912 |
| sharpe_ratio | 0.2404 |
| sortino_ratio | 0.0427 |
| max_drawdown | 0.1203 |
| cagr | 0.0155 |
| net_avg_win | 91.8333 |
| net_avg_loss | -126.2547 |
| avg_hold_time_bars | 4.3577 |
| exposure | 0.0289 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
