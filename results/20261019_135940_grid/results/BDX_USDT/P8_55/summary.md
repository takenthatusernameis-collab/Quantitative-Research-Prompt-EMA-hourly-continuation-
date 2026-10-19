# EMA Hourly Continuation — BDX/USDT P8_55

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1676 |
| net_profit_factor | 0.3010 |
| net_win_rate | 0.2709 |
| gross_profit_factor | 0.6840 |
| gross_win_rate | 0.3192 |
| sharpe_ratio | -21.2777 |
| sortino_ratio | -12.9557 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 9.4861 |
| net_avg_loss | -11.7076 |
| avg_hold_time_bars | 4.2428 |
| exposure | 0.3232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
