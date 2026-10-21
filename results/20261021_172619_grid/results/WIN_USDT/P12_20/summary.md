# EMA Hourly Continuation — WIN/USDT P12_20

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.7090 |
| net_win_rate | 0.5417 |
| gross_profit_factor | 1.1946 |
| gross_win_rate | 0.5417 |
| sharpe_ratio | -1.8319 |
| sortino_ratio | -0.4520 |
| max_drawdown | 0.4251 |
| cagr | -0.1844 |
| net_avg_win | 62.5804 |
| net_avg_loss | -104.3121 |
| avg_hold_time_bars | 5.4097 |
| exposure | 0.0708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
