# EMA Hourly Continuation — AMP/USDT P12_50

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.4772 |
| net_win_rate | 0.3890 |
| gross_profit_factor | 0.6448 |
| gross_win_rate | 0.3890 |
| sharpe_ratio | -6.3199 |
| sortino_ratio | -2.3798 |
| max_drawdown | 0.9392 |
| cagr | -0.6685 |
| net_avg_win | 31.1205 |
| net_avg_loss | -41.5127 |
| avg_hold_time_bars | 9.0990 |
| exposure | 0.2924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
