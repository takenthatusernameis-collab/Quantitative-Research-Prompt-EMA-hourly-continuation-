# EMA Hourly Continuation — POL/USDT P12_34

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1317 |
| net_profit_factor | 0.3579 |
| net_win_rate | 0.4123 |
| gross_profit_factor | 0.7940 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -11.2686 |
| sortino_ratio | -5.7738 |
| max_drawdown | 0.9994 |
| cagr | -0.9463 |
| net_avg_win | 10.2568 |
| net_avg_loss | -20.1072 |
| avg_hold_time_bars | 4.3766 |
| exposure | 0.2620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
