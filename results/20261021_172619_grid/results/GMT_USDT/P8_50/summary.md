# EMA Hourly Continuation — GMT/USDT P8_50

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.6985 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.8945 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -2.7563 |
| sortino_ratio | -1.0331 |
| max_drawdown | 0.7128 |
| cagr | -0.3776 |
| net_avg_win | 48.8631 |
| net_avg_loss | -64.1259 |
| avg_hold_time_bars | 13.6522 |
| exposure | 0.4282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
