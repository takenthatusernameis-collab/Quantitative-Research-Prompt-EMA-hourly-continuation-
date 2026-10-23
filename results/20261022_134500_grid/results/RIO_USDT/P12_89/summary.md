# EMA Hourly Continuation — RIO/USDT P12_89

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.6701 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -4.4699 |
| sortino_ratio | -1.8641 |
| max_drawdown | 0.8952 |
| cagr | -0.5917 |
| net_avg_win | 45.2962 |
| net_avg_loss | -56.6885 |
| avg_hold_time_bars | 12.5735 |
| exposure | 0.5062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
