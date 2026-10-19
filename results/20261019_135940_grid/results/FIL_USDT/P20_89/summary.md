# EMA Hourly Continuation — FIL/USDT P20_89

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.4817 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.7846 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -5.9770 |
| sortino_ratio | -2.2579 |
| max_drawdown | 0.9396 |
| cagr | -0.6656 |
| net_avg_win | 27.8017 |
| net_avg_loss | -44.0566 |
| avg_hold_time_bars | 11.1328 |
| exposure | 0.3659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
