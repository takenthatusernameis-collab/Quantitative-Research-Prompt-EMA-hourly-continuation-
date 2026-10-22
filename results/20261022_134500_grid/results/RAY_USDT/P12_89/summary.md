# EMA Hourly Continuation — RAY/USDT P12_89

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.6723 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.8387 |
| sortino_ratio | -1.4564 |
| max_drawdown | 0.8363 |
| cagr | -0.5013 |
| net_avg_win | 48.6849 |
| net_avg_loss | -66.3149 |
| avg_hold_time_bars | 15.3104 |
| exposure | 0.5066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
