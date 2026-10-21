# EMA Hourly Continuation — XCN/USDT P20_89

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -2.4841 |
| sortino_ratio | -0.7835 |
| max_drawdown | 0.6024 |
| cagr | -0.3033 |
| net_avg_win | 62.1124 |
| net_avg_loss | -78.6708 |
| avg_hold_time_bars | 15.3585 |
| exposure | 0.3428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
