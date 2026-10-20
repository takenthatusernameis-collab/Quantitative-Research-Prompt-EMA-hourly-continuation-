# EMA Hourly Continuation — AMP/USDT P89_200

**Symbol:** AMP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.3568 |
| net_win_rate | 0.3893 |
| gross_profit_factor | 0.5991 |
| gross_win_rate | 0.4008 |
| sharpe_ratio | -6.2685 |
| sortino_ratio | -2.0309 |
| max_drawdown | 0.9180 |
| cagr | -0.6259 |
| net_avg_win | 24.8936 |
| net_avg_loss | -44.4734 |
| avg_hold_time_bars | 10.0878 |
| exposure | 0.2403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
