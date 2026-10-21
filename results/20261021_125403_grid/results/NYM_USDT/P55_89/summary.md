# EMA Hourly Continuation — NYM/USDT P55_89

**Symbol:** NYM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.3711 |
| net_win_rate | 0.3952 |
| gross_profit_factor | 0.6495 |
| gross_win_rate | 0.3992 |
| sharpe_ratio | -4.3964 |
| sortino_ratio | -0.9935 |
| max_drawdown | 0.6927 |
| cagr | -0.3719 |
| net_avg_win | 41.4770 |
| net_avg_loss | -73.0271 |
| avg_hold_time_bars | 9.4718 |
| exposure | 0.1068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
