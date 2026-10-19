# EMA Hourly Continuation — MNT/USDT P89_144

**Symbol:** MNT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.3712 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.7856 |
| gross_win_rate | 0.4491 |
| sharpe_ratio | -5.7688 |
| sortino_ratio | -1.7054 |
| max_drawdown | 0.8794 |
| cagr | -0.5677 |
| net_avg_win | 28.0257 |
| net_avg_loss | -56.5493 |
| avg_hold_time_bars | 6.2546 |
| exposure | 0.1228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
