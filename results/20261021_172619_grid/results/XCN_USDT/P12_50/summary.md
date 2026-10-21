# EMA Hourly Continuation — XCN/USDT P12_50

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.7010 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.7151 |
| sortino_ratio | -0.9444 |
| max_drawdown | 0.6732 |
| cagr | -0.3523 |
| net_avg_win | 54.8255 |
| net_avg_loss | -71.4168 |
| avg_hold_time_bars | 10.8437 |
| exposure | 0.2933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
