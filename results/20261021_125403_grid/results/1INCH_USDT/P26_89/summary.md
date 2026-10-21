# EMA Hourly Continuation — 1INCH/USDT P26_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6856 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9114 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -2.9029 |
| sortino_ratio | -0.9435 |
| max_drawdown | 0.6747 |
| cagr | -0.3516 |
| net_avg_win | 59.0123 |
| net_avg_loss | -77.2474 |
| avg_hold_time_bars | 13.3842 |
| exposure | 0.3151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
