# EMA Hourly Continuation — MOVR/USDT P12_34

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.6595 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8895 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.2059 |
| sortino_ratio | -1.1980 |
| max_drawdown | 0.7652 |
| cagr | -0.4223 |
| net_avg_win | 44.3060 |
| net_avg_loss | -61.5318 |
| avg_hold_time_bars | 6.5863 |
| exposure | 0.2048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
