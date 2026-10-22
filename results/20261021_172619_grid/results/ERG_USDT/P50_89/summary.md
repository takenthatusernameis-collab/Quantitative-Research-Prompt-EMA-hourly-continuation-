# EMA Hourly Continuation — ERG/USDT P50_89

**Symbol:** ERG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.4844 |
| net_win_rate | 0.3883 |
| gross_profit_factor | 0.6543 |
| gross_win_rate | 0.3883 |
| sharpe_ratio | -3.8100 |
| sortino_ratio | -0.8914 |
| max_drawdown | 0.6444 |
| cagr | -0.3375 |
| net_avg_win | 57.1174 |
| net_avg_loss | -74.8437 |
| avg_hold_time_bars | 11.0403 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
