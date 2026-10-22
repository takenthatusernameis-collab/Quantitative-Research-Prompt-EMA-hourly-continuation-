# EMA Hourly Continuation — BSV/USDT P21_50

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.3619 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8241 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -10.0134 |
| sortino_ratio | -4.6676 |
| max_drawdown | 0.9976 |
| cagr | -0.9081 |
| net_avg_win | 12.4614 |
| net_avg_loss | -24.3119 |
| avg_hold_time_bars | 4.2871 |
| exposure | 0.2138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
