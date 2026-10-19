# EMA Hourly Continuation — ZRO/USDT P26_89

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6776 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9776 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.5095 |
| sortino_ratio | -1.3353 |
| max_drawdown | 0.7781 |
| cagr | -0.4714 |
| net_avg_win | 49.5837 |
| net_avg_loss | -68.5775 |
| avg_hold_time_bars | 9.4735 |
| exposure | 0.3144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
