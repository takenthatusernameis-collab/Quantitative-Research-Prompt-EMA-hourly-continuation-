# EMA Hourly Continuation — BSV/USDT P8_89

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 879 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4221 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -7.2346 |
| sortino_ratio | -2.9764 |
| max_drawdown | 0.9781 |
| cagr | -0.7772 |
| net_avg_win | 26.9094 |
| net_avg_loss | -38.8841 |
| avg_hold_time_bars | 15.2241 |
| exposure | 0.6083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
