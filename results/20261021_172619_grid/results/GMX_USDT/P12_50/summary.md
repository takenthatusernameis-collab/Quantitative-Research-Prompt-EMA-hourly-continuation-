# EMA Hourly Continuation — GMX/USDT P12_50

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.9140 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -3.3775 |
| sortino_ratio | -1.2821 |
| max_drawdown | 0.7748 |
| cagr | -0.4442 |
| net_avg_win | 49.7583 |
| net_avg_loss | -65.1905 |
| avg_hold_time_bars | 10.7560 |
| exposure | 0.3466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
