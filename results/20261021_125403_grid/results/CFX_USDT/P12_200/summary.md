# EMA Hourly Continuation — CFX/USDT P12_200

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8509 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -0.8628 |
| sortino_ratio | -0.2057 |
| max_drawdown | 0.2747 |
| cagr | -0.0919 |
| net_avg_win | 87.6356 |
| net_avg_loss | -104.4792 |
| avg_hold_time_bars | 59.3849 |
| exposure | 0.7504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
