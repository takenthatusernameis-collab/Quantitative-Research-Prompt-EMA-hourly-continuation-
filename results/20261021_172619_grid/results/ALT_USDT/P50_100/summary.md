# EMA Hourly Continuation — ALT/USDT P50_100

**Symbol:** ALT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7082 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.9876 |
| sortino_ratio | -0.5641 |
| max_drawdown | 0.4919 |
| cagr | -0.2280 |
| net_avg_win | 60.3904 |
| net_avg_loss | -81.0554 |
| avg_hold_time_bars | 9.6701 |
| exposure | 0.1732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
