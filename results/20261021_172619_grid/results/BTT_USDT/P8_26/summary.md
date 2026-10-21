# EMA Hourly Continuation — BTT/USDT P8_26

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5077 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -6.7902 |
| sortino_ratio | -2.5141 |
| max_drawdown | 0.9488 |
| cagr | -0.6931 |
| net_avg_win | 34.0797 |
| net_avg_loss | -52.0701 |
| avg_hold_time_bars | 7.7458 |
| exposure | 0.2313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
