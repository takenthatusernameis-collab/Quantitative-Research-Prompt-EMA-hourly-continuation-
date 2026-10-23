# EMA Hourly Continuation — CTSI/USDT P8_26

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1412 |
| net_profit_factor | 0.4947 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -8.3688 |
| sortino_ratio | -4.4565 |
| max_drawdown | 0.9955 |
| cagr | -0.8832 |
| net_avg_win | 14.9472 |
| net_avg_loss | -25.9211 |
| avg_hold_time_bars | 4.7925 |
| exposure | 0.3076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
