# EMA Hourly Continuation — JST/USDT P21_89

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.3985 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 1.0624 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -6.0558 |
| sortino_ratio | -2.1042 |
| max_drawdown | 0.9377 |
| cagr | -0.6644 |
| net_avg_win | 21.3198 |
| net_avg_loss | -46.0582 |
| avg_hold_time_bars | 13.2528 |
| exposure | 0.3772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
