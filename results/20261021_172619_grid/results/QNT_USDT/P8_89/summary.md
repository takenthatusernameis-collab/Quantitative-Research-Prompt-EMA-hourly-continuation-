# EMA Hourly Continuation — QNT/USDT P8_89

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.7945 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0337 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -1.5929 |
| sortino_ratio | -0.5796 |
| max_drawdown | 0.5339 |
| cagr | -0.2357 |
| net_avg_win | 57.3279 |
| net_avg_loss | -77.0448 |
| avg_hold_time_bars | 18.3822 |
| exposure | 0.5356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
