# EMA Hourly Continuation — NYM/USDT P12_50

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.3071 |
| net_win_rate | 0.3744 |
| gross_profit_factor | 0.7123 |
| gross_win_rate | 0.4050 |
| sharpe_ratio | -10.6778 |
| sortino_ratio | -4.5031 |
| max_drawdown | 0.9974 |
| cagr | -0.9057 |
| net_avg_win | 13.3515 |
| net_avg_loss | -26.0268 |
| avg_hold_time_bars | 10.5419 |
| exposure | 0.4236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
