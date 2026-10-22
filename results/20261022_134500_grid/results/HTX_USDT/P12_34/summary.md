# EMA Hourly Continuation — HTX/USDT P12_34

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1393 |
| net_profit_factor | 0.1624 |
| net_win_rate | 0.2793 |
| gross_profit_factor | 0.5758 |
| gross_win_rate | 0.3632 |
| sharpe_ratio | -19.1126 |
| sortino_ratio | -10.7302 |
| max_drawdown | 1.0000 |
| cagr | -0.9971 |
| net_avg_win | 4.9828 |
| net_avg_loss | -11.8907 |
| avg_hold_time_bars | 4.6253 |
| exposure | 0.2916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
