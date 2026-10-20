# EMA Hourly Continuation — WEMIX/USDT P8_34

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1898 |
| net_profit_factor | 0.1977 |
| net_win_rate | 0.3093 |
| gross_profit_factor | 0.4285 |
| gross_win_rate | 0.3277 |
| sharpe_ratio | -19.0721 |
| sortino_ratio | -11.8976 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 4.1971 |
| net_avg_loss | -9.5070 |
| avg_hold_time_bars | 4.4463 |
| exposure | 0.3836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
