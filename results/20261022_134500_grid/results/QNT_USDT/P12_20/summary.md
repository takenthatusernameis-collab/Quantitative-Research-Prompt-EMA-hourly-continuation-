# EMA Hourly Continuation — QNT/USDT P12_20

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1575 |
| net_profit_factor | 0.1560 |
| net_win_rate | 0.3670 |
| gross_profit_factor | 0.5883 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -16.2125 |
| sortino_ratio | -9.3479 |
| max_drawdown | 1.0000 |
| cagr | -0.9927 |
| net_avg_win | 3.1979 |
| net_avg_loss | -11.8840 |
| avg_hold_time_bars | 2.1708 |
| exposure | 0.1554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
