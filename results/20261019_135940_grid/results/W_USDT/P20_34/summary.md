# EMA Hourly Continuation — W/USDT P20_34

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1145 |
| net_profit_factor | 0.5504 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 1.0265 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -8.2849 |
| sortino_ratio | -3.9641 |
| max_drawdown | 0.9927 |
| cagr | -0.8582 |
| net_avg_win | 23.5515 |
| net_avg_loss | -35.1010 |
| avg_hold_time_bars | 2.8961 |
| exposure | 0.1507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
