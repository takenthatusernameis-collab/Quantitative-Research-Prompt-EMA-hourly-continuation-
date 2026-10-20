# EMA Hourly Continuation — DGB/USDT P12_21

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.3052 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.8503 |
| gross_win_rate | 0.4076 |
| sharpe_ratio | -15.2670 |
| sortino_ratio | -8.7041 |
| max_drawdown | 1.0000 |
| cagr | -0.9899 |
| net_avg_win | 7.2981 |
| net_avg_loss | -14.4657 |
| avg_hold_time_bars | 2.3206 |
| exposure | 0.1685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
