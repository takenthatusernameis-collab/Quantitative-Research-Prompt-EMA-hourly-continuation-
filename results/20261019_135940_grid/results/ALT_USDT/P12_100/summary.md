# EMA Hourly Continuation — ALT/USDT P12_100

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.7115 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9591 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.5859 |
| sortino_ratio | -0.9088 |
| max_drawdown | 0.6764 |
| cagr | -0.3481 |
| net_avg_win | 53.4311 |
| net_avg_loss | -72.7026 |
| avg_hold_time_bars | 20.3026 |
| exposure | 0.5703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
