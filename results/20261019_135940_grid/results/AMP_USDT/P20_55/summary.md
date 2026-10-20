# EMA Hourly Continuation — AMP/USDT P20_55

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1344 |
| net_profit_factor | 0.3494 |
| net_win_rate | 0.3757 |
| gross_profit_factor | 0.6979 |
| gross_win_rate | 0.3921 |
| sharpe_ratio | -12.5322 |
| sortino_ratio | -6.5250 |
| max_drawdown | 0.9997 |
| cagr | -0.9615 |
| net_avg_win | 10.6326 |
| net_avg_loss | -18.3154 |
| avg_hold_time_bars | 4.4903 |
| exposure | 0.2743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
