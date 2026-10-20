# EMA Hourly Continuation — ONT/USDT P12_26

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1348 |
| net_profit_factor | 0.3966 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.8830 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -12.0814 |
| sortino_ratio | -6.2424 |
| max_drawdown | 0.9997 |
| cagr | -0.9619 |
| net_avg_win | 11.9037 |
| net_avg_loss | -20.8144 |
| avg_hold_time_bars | 3.1113 |
| exposure | 0.1898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
