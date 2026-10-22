# EMA Hourly Continuation — TRX/USDT P55_89

**Symbol:** TRX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.1697 |
| net_win_rate | 0.3138 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -11.7891 |
| sortino_ratio | -4.4134 |
| max_drawdown | 0.9975 |
| cagr | -0.9079 |
| net_avg_win | 10.9057 |
| net_avg_loss | -29.3748 |
| avg_hold_time_bars | 4.4497 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
