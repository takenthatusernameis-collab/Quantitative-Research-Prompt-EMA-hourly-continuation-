# EMA Hourly Continuation — ZPAY/USDT P8_34

**Symbol:** ZPAY/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.4402 |
| net_win_rate | 0.3330 |
| gross_profit_factor | 0.6666 |
| gross_win_rate | 0.3380 |
| sharpe_ratio | -9.5186 |
| sortino_ratio | -4.1986 |
| max_drawdown | 0.9932 |
| cagr | -0.8621 |
| net_avg_win | 23.4572 |
| net_avg_loss | -26.6022 |
| avg_hold_time_bars | 8.3870 |
| exposure | 0.3795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
