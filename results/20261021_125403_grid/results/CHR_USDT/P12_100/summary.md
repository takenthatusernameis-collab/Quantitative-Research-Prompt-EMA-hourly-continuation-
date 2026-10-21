# EMA Hourly Continuation — CHR/USDT P12_100

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.8148 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9682 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.4021 |
| sortino_ratio | -0.4267 |
| max_drawdown | 0.4160 |
| cagr | -0.1805 |
| net_avg_win | 77.5242 |
| net_avg_loss | -91.8631 |
| avg_hold_time_bars | 29.5219 |
| exposure | 0.6092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
