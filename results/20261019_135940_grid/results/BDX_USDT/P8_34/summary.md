# EMA Hourly Continuation — BDX/USDT P8_34

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1837 |
| net_profit_factor | 0.2626 |
| net_win_rate | 0.2444 |
| gross_profit_factor | 0.6803 |
| gross_win_rate | 0.3038 |
| sharpe_ratio | -24.0125 |
| sortino_ratio | -15.6233 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 7.9305 |
| net_avg_loss | -9.7700 |
| avg_hold_time_bars | 2.9804 |
| exposure | 0.2489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
