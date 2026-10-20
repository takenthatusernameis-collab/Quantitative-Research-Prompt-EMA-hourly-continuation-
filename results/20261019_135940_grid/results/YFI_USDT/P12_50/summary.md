# EMA Hourly Continuation — YFI/USDT P12_50

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1207 |
| net_profit_factor | 0.4130 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -9.7771 |
| sortino_ratio | -4.8090 |
| max_drawdown | 0.9975 |
| cagr | -0.9056 |
| net_avg_win | 13.8391 |
| net_avg_loss | -24.2721 |
| avg_hold_time_bars | 6.3181 |
| exposure | 0.3451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
