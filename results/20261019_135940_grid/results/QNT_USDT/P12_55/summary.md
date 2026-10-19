# EMA Hourly Continuation — QNT/USDT P12_55

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1203 |
| net_profit_factor | 0.4274 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -8.3326 |
| sortino_ratio | -4.0615 |
| max_drawdown | 0.9938 |
| cagr | -0.8667 |
| net_avg_win | 13.7366 |
| net_avg_loss | -26.1754 |
| avg_hold_time_bars | 6.0740 |
| exposure | 0.3321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
