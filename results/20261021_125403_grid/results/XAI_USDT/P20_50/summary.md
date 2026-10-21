# EMA Hourly Continuation — XAI/USDT P20_50

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9082 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.9323 |
| sortino_ratio | -1.0113 |
| max_drawdown | 0.7018 |
| cagr | -0.3712 |
| net_avg_win | 61.0144 |
| net_avg_loss | -76.5205 |
| avg_hold_time_bars | 7.8771 |
| exposure | 0.2098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
