# EMA Hourly Continuation — UMA/USDT P34_144

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7838 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 0.9921 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.4646 |
| sortino_ratio | -0.4172 |
| max_drawdown | 0.4077 |
| cagr | -0.1747 |
| net_avg_win | 69.6969 |
| net_avg_loss | -89.8254 |
| avg_hold_time_bars | 22.1894 |
| exposure | 0.3994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
