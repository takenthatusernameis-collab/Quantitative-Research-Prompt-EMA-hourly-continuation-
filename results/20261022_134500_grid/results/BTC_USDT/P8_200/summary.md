# EMA Hourly Continuation — BTC/USDT P8_200

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.4876 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.9254 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -3.8969 |
| sortino_ratio | -0.9801 |
| max_drawdown | 0.7591 |
| cagr | -0.3927 |
| net_avg_win | 42.7487 |
| net_avg_loss | -71.9181 |
| avg_hold_time_bars | 55.0773 |
| exposure | 0.8262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
