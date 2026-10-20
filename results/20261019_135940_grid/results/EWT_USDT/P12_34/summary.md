# EMA Hourly Continuation — EWT/USDT P12_34

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1134 |
| net_profit_factor | 0.3460 |
| net_win_rate | 0.3633 |
| gross_profit_factor | 0.6290 |
| gross_win_rate | 0.3862 |
| sharpe_ratio | -11.7496 |
| sortino_ratio | -5.5921 |
| max_drawdown | 0.9993 |
| cagr | -0.9435 |
| net_avg_win | 12.8317 |
| net_avg_loss | -21.1625 |
| avg_hold_time_bars | 4.2866 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
