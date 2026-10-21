# EMA Hourly Continuation — SUI/USDT P12_89

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7992 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.5913 |
| sortino_ratio | -0.4980 |
| max_drawdown | 0.4904 |
| cagr | -0.2061 |
| net_avg_win | 74.5257 |
| net_avg_loss | -89.4409 |
| avg_hold_time_bars | 22.5000 |
| exposure | 0.4909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
