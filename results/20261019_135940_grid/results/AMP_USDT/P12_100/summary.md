# EMA Hourly Continuation — AMP/USDT P12_100

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.3759 |
| net_win_rate | 0.3831 |
| gross_profit_factor | 0.6419 |
| gross_win_rate | 0.3975 |
| sharpe_ratio | -9.3302 |
| sortino_ratio | -4.2211 |
| max_drawdown | 0.9947 |
| cagr | -0.8739 |
| net_avg_win | 15.0503 |
| net_avg_loss | -24.8594 |
| avg_hold_time_bars | 11.2772 |
| exposure | 0.5326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
