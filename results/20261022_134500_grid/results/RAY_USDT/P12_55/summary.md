# EMA Hourly Continuation — RAY/USDT P12_55

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.6074 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.9041 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -5.8488 |
| sortino_ratio | -2.6146 |
| max_drawdown | 0.9590 |
| cagr | -0.7155 |
| net_avg_win | 32.4067 |
| net_avg_loss | -43.7778 |
| avg_hold_time_bars | 7.7337 |
| exposure | 0.3565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
