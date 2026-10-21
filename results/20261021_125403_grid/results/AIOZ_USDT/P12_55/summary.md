# EMA Hourly Continuation — AIOZ/USDT P12_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.8078 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9830 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.0177 |
| sortino_ratio | -0.7489 |
| max_drawdown | 0.6072 |
| cagr | -0.2929 |
| net_avg_win | 73.7884 |
| net_avg_loss | -87.8965 |
| avg_hold_time_bars | 10.9067 |
| exposure | 0.3346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
