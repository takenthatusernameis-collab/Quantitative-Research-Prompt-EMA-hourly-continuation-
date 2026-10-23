# EMA Hourly Continuation — POPCAT/USDT P12_20

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1318 |
| net_profit_factor | 0.4509 |
| net_win_rate | 0.4044 |
| gross_profit_factor | 0.7457 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -11.8527 |
| sortino_ratio | -6.5852 |
| max_drawdown | 0.9991 |
| cagr | -0.9618 |
| net_avg_win | 15.3931 |
| net_avg_loss | -23.1795 |
| avg_hold_time_bars | 2.1950 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
