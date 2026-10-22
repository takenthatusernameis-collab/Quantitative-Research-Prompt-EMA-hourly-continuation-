# EMA Hourly Continuation — RIO/USDT P12_89

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.8914 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0046 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8674 |
| sortino_ratio | -0.2904 |
| max_drawdown | 0.3699 |
| cagr | -0.1301 |
| net_avg_win | 88.6693 |
| net_avg_loss | -99.4745 |
| avg_hold_time_bars | 18.9926 |
| exposure | 0.4726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
