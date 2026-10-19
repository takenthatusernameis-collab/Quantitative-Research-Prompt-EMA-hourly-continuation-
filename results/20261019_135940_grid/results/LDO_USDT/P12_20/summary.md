# EMA Hourly Continuation — LDO/USDT P12_20

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1535 |
| net_profit_factor | 0.2843 |
| net_win_rate | 0.3739 |
| gross_profit_factor | 0.6746 |
| gross_win_rate | 0.4072 |
| sharpe_ratio | -14.4424 |
| sortino_ratio | -8.0628 |
| max_drawdown | 1.0000 |
| cagr | -0.9849 |
| net_avg_win | 6.9188 |
| net_avg_loss | -14.5381 |
| avg_hold_time_bars | 1.9896 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
